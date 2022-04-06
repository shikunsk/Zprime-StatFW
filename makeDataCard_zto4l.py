import os,copy,math,argparse,ROOT,re,numpy

from CombineStatFW.DataCard import DataCard,CardConfig
from CombineStatFW.Systematic import *
from CombineStatFW.Process import *
from CombineStatFW.Reader import *
from CombineStatFW.Channel import Bin
from CombineStatFW.FileReader import FileReader
from CombineStatFW.RateParameter import RateParameter
#from CombineStatFW.BaseObject import BaseObject

from Utils.Hist import getCountAndError,getIntegral
from Utils.DataCard import SignalModel
from Utils.mkdir_p import mkdir_p

# ____________________________________________________________________________________________________________________________________________ ||
parser = argparse.ArgumentParser()
parser.add_argument("--inputDir",action="store")
parser.add_argument("--outputDir",action="store")
parser.add_argument("--verbose",action="store_true")
parser.add_argument("--elWidth",action="store",type=float,default=0.05)
parser.add_argument("--muWidth",action="store",type=float,default=0.02)
parser.add_argument("--appendToPath",action="store")

option = parser.parse_args()

# ____________________________________________________________________________________________________________________________________________ ||
# Configurable
inputDir = option.inputDir
#commonLnSystFilePath = "/home/lucien/Higgs/DarkZ/DarkZ-StatFW/Config/CommonSyst_2mu2e.txt"
commonLnSystFilePath = "/home/kshi/SUSY/CMSSW_8_0_25/src/Zprime-StatFW/Config/CommonSyst_2mu2e_Zprime.txt" 
lnSystFilePathDict = {
        #"TwoMu": "/home/lucien/Higgs/DarkZ/DarkZ-StatFW/Config/Syst_2mu.txt", 
        #"TwoEl": "/home/lucien/Higgs/DarkZ/DarkZ-StatFW/Config/Syst_2e.txt", 
        "TwoMu": "/home/kshi/SUSY/CMSSW_8_0_25/src/Zprime-StatFW/Config/Syst_2mu_Run2018.txt",
        "TwoEl": "/home/kshi/SUSY/CMSSW_8_0_25/src/Zprime-StatFW/Config/Syst_2e_Run2018.txt",
        }
outputDir = option.outputDir
TFileName = "StatInput.root"
isSRFunc = lambda x: x.name.endswith("SR")
fitfunc = True

# ____________________________________________________________________________________________________________________________________________ ||
# mass window
'''
mass_points = [
        #1,
        5,
        10,
        15,
        ] + range(20,80,10)
'''
'''
mass_points = [
        5,
        70,
        ] + range(6,70,1)

'''
'''
mass_points = [
        5,
        70,
        ] + list(numpy.arange(5.01,15,0.01)) + list(numpy.arange(15,25,0.02)) + list(numpy.arange(25,55,0.05)) + list(numpy.arange(55,70,0.1))
'''

mass_points = [
        5,
        70,
        ] + list(numpy.arange(5.01,15,0.02)) + list(numpy.arange(15,25,0.05)) + list(numpy.arange(25,55,0.1)) + list(numpy.arange(55,70,0.2))

signal_models = [ 
        SignalModel("ZpToMuMu_M"+str(m),["zpToMuMu_M"+str(m),],m) for m in mass_points
        #SignalModel("ZpTo3munu_ZpM"+str(m),["zpTo3munuMu_ZpM"+str(m),],m) for m in mass_points
        #SignalModel("ZmTo3munu_ZpM"+str(m),["zmTo3munuMu_ZpM"+str(m),],m) for m in mass_points
        #SignalModel("WTo3munu_ZpM15",["WpTo3munu_ZpM15","WmTo3munu_ZpM15",],15),
        #SignalModel("WTo3munu_ZpM20",["WpTo3munu_ZpM20","WmTo3munu_ZpM20",],20),
        #SignalModel("WTo3munu_ZpM30",["WpTo3munu_ZpM30","WmTo3munu_ZpM30",],30),
        #SignalModel("WTo3munu_ZpM45",["WpTo3munu_ZpM45","WmTo3munu_ZpM45",],45),
        #SignalModel("WTo3munu_ZpM60",["WpTo3munu_ZpM60","WmTo3munu_ZpM60",],60),
        #SignalModel("WpTo3munu_ZpM15",["WpTo3munu_ZpM15",],15),
        #SignalModel("WmTo3munu_ZpM15",["WmTo3munu_ZpM15",],15),
        ]

data_names = [
        "Data2016",
        #"Data2017",
        #"Data2018",
        #BaseObject("Data"),
        ]

bkg_names = [
        #"qqZZTo4L_M1To4",
        #"ZPlusX",
        "ggZZ",
        #"Higgs",
        "qqZZ",
        #BaseObject("ggZZ"),
        #BaseObject("qqZZ"),
        #BaseObject("Higgs"),
        ]

# ____________________________________________________________________________________________________________________________________________ ||
# bin list

binList = [
        Bin("FourMu_SR",signalNames=["zpToMuMu",],sysFile=lnSystFilePathDict["TwoMu"],inputBinName="",width=option.muWidth,inputBinNameFunc=lambda x: "mZ2_4mu" if x.central_value <= 42.5 else "mZ1_4mu"),
        ]
'''
binList = [
        Bin("NNP",signalNames=["WpTo3munu","WmTo3munu"],sysFile=lnSystFilePathDict["NNP"],inputBinName="NNP_mass2",width=option.muWidth),
        Bin("PPN",signalNames=["WpTo3munu","WmTo3munu"],sysFile=lnSystFilePathDict["PPN"],inputBinName="PPN_mass2",width=option.muWidth),
        ]
'''
# ____________________________________________________________________________________________________________________________________________ ||
# syst
lnSystReader = LogNormalSystReader()
commonLnSystematics = lnSystReader.makeLnSyst(commonLnSystFilePath)

# ____________________________________________________________________________________________________________________________________________ ||
reader = FileReader()

mkdir_p(os.path.abspath(outputDir))

for signal_model in signal_models:
    signal_model_name = signal_model.name
    if option.verbose: print "*"*100
    if option.verbose: print "Making data card for ",signal_model_name
    central_value = signal_model.central_value
    binListCopy = [b for b in copy.deepcopy(binList) ]
    for ibin,bin in enumerate(binListCopy):
        if option.verbose: print "-"*20
        if option.verbose: print bin.name
        histName = bin.inputBinName if not bin.inputBinNameFunc else bin.inputBinNameFunc(signal_model) 

        # bkg
        for bkgName in bkg_names:
            reader.openFile(inputDir,bkgName,TFileName)
            hist = reader.getObj(bkgName,histName)
            count,error = getCountAndError(hist,central_value,bin.width,isSR=True)
            process = Process(bkgName,count if count >= 0. else 1e-12,error)
            bin.processList.append(process)

        # data
        dataCount = 0.
        for sample in data_names:
            reader.openFile(inputDir,sample,TFileName)
            hist = reader.getObj(sample,histName)
            count,error = getCountAndError(hist,central_value,bin.width,isSR=True)
            dataCount += count
        error = math.sqrt(dataCount)
        bin.data = Process("data_obs",int(dataCount),error)
        
        bin.systList = []
        
        # signal
        for each_signal_model_name in signal_model.signal_list:
            if not fitfunc:
                reader.openFile(inputDir,each_signal_model_name,TFileName)
                hist = reader.getObj(each_signal_model_name,histName)
                count,error = copy.deepcopy(getCountAndError(hist,central_value,bin.width,isSR=True))
                bin.processList.append(Process(each_signal_model_name,count if count >= 0. else 1e-12,error))
            else:
                #for key in bin.interFuncDict:
                    #if key in each_signal_model_name: break
                #count = bin.interFuncDict[key].Eval(central_value)
                snum = re.search('\d+', signal_model_name).group()
                num = int(snum)
                if num <= 42.5:
                    if option.appendToPath == "2016":
                        count = math.exp(7.83452 - 0.0773427*num + 0.00136481*num*num - 0.0000461371*num*num*num)*35.9/41.4
                    if option.appendToPath == "2017":
                        count = math.exp(7.83452 - 0.0773427*num + 0.00136481*num*num - 0.0000461371*num*num*num)
                    if option.appendToPath == "2018":
                        count = math.exp(8.22146 - 0.0856628*num + 0.00159842*num*num - 0.0000484742*num*num*num)
                if num > 42.5:
                    if option.appendToPath == "2016":
                        count = math.exp(-10.426 + 0.689723*num - 0.00934949*num*num + 0.0000230266*num*num*num)*35.9/41.4
                    if option.appendToPath == "2017":
                        count = math.exp(-10.426 + 0.689723*num - 0.00934949*num*num + 0.0000230266*num*num*num)
                    if option.appendToPath == "2018":
                        count = math.exp(-11.6038 + 0.198406*num + 0.0317723*num*num - 0.00113849*num*num*num + 0.0000140668*num*num*num*num - 0.0000000623929*num*num*num*num*num)
                #count = count * 0.25
                bin.processList.append(Process(each_signal_model_name,count if count >= 0. else 1e-12,error))
            # systematics
            '''
            if count: 
                mcSyst = lnNSystematic("SigStat_"+bin.name,[ each_signal_model_name, ],lambda syst,procName,anaBin: float(1.+error/count))
                bin.systList.append(mcSyst)
            '''
        
        for syst in commonLnSystematics:
            bin.systList.append(copy.deepcopy(syst))
        bin.systList += lnSystReader.makeLnSyst(bin.sysFile)

    config = CardConfig(signal_model_name)
    dataCard = DataCard(config) 
    cardDir = outputDir+"/"+dataCard.makeOutFileName("/","")
    mkdir_p(cardDir)
    #dataCard.makeCard(cardDir,binListCopy)
    dataCard.makeCard(cardDir,[bin],appendToPath=option.appendToPath if option.appendToPath else "")
    reader.end()
