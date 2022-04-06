import ROOT,glob,os,argparse,subprocess,array,math
from collections import OrderedDict
import Utils.CMS_lumi as CMS_lumi
import Utils.tdrstyle as tdrstyle
from Utils.mkdir_p import mkdir_p
import numpy as np

ROOT.gROOT.SetBatch(ROOT.kTRUE)

parser = argparse.ArgumentParser()
parser.add_argument("--inputDir",action="store")
parser.add_argument("--outputPath",action="store")
parser.add_argument("--selectStr",action="store",default="")

option = parser.parse_args()

inputDir = option.inputDir

# ________________________________________________________________ ||
# CMS style
# ________________________________________________________________ ||
CMS_lumi.cmsText = "CMS"
#CMS_lumi.extraText = "Preliminary"
CMS_lumi.extraText = "Work in Progress"
CMS_lumi.cmsTextSize = 0.65
CMS_lumi.outOfFrame = False
#CMS_lumi.drawLogo = True
#CMS_lumi.lumi_13TeV = "77.3 fb^{-1}"
#CMS_lumi.lumi_13TeV = "35.9 fb^{-1}"
#CMS_lumi.lumi_13TeV = "41.4 fb^{-1}"
#CMS_lumi.lumi_13TeV = "59.7 fb^{-1}"
#CMS_lumi.lumi_13TeV = "136.1 fb^{-1}"
#CMS_lumi.lumi_13TeV = "150 fb^{-1}"
CMS_lumi.lumi_13TeV = "137 fb^{-1}"
tdrstyle.setTDRStyle()

setLogY         = True
expOnly         = True 
quantiles       = ["down2","down1","central","up1","up2","obs"]
#quantiles       = ["down2","down1","central","up1","up2",]
varName         = "limit"
plots           = ["co",]
maxFactor       = 1.5
draw_theory     = False
y_label_dict    = {
                    "r": "95% upper limit on Signal strength",
                    "xs": "95% upper limit on cross section",
                    "co": "95% upper limit on coupling",
                  }
x_label         = "Z^{'} mass"
xsec            = {
                    1: 5.715,
                    2: 2.311,
                    3: 1.403,
                    4: 0.7584,
                    5: 0.5555,
                    10: 0.2173,
                    15: 0.1141,
                    20: 0.0650,
                    25: 0.0382,
                    30: 0.0226,
                    35: 0.0134,
                    40: 0.0079,
                    45: 0.0045,
                    50: 0.0025,
                    55: 0.0014,
                    60: 0.0007,
                    65: 0.0004,
                    70: 0.0002,
                    75: 0.0001406, 
                    80: 0.0001018,
                    85: 0.00008061,
                    90: 0.0000666,
                   }

def calculate(r_value,window_value,what):
    if what == "r":
        return r_value 
    elif what == "xs":
        #return r_value*xsec[model+'_M'+str(window_value)]
        #return r_value*xsec[int(window_value)]
        #return r_value*math.exp(0.000000000532862*math.pow(window_value,6)-0.000000164830851*math.pow(window_value,5)+0.000020233298164*math.pow(window_value,4)-0.001232799273215*math.pow(window_value,3)+0.038020361596005*math.pow(window_value,2)-0.646870016200233*window_value+2.03534644170333)
        return r_value*math.exp(0.0000004936*math.pow(window_value,4)-0.000089271*math.pow(window_value,3)+0.0053650056*math.pow(window_value,2)-0.2349086721*window_value+0.4302015825)*3
    elif what == "co":
        return np.sqrt(r_value)/10.0
    else:
        raise RuntimeError

# ________________________________________________________________ ||
# Read limit from directory
# ________________________________________________________________ ||
outDict = OrderedDict()
for quantile in quantiles:
    outDict[quantile] = OrderedDict()
for cardDir in glob.glob(inputDir+"*"+option.selectStr+"*/"):
    #print "Reading directory "+cardDir
    inputFile = ROOT.TFile(cardDir+"higgsCombineTest.AsymptoticLimits.mH120.root","READ")
    tree = inputFile.Get("limit")
    window_name = cardDir.split("/")[-2]
    #window_value = int(window_name.split("_Zp")[1][1:])
    #window_value = int(window_name.split("_M")[1][0:])
    window_value = float(window_name.split("_M")[1][0:])
    if expOnly:
        for i,entry in enumerate(tree):
            outDict[quantiles[i]][window_value] = getattr(entry,varName)
    else:
        raise RuntimeError

# ________________________________________________________________ ||
# Draw limit with outDict
# ________________________________________________________________ ||
mkdir_p(os.path.dirname(option.outputPath))
nPoints = len(outDict["central"])
outGraphDict = {}
for plot in plots:
    W = 800
    H  = 600
    T = 0.08*H
    B = 0.12*H
    L = 0.12*W
    R = 0.04*W
    c = ROOT.TCanvas("c","c",100,100,W,H)
    if setLogY:
        c.SetLogy()
        #c.SetLogx()
    c.SetFillColor(0)
    c.SetBorderMode(0)
    c.SetFrameFillStyle(0)
    c.SetFrameBorderMode(0)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    c.SetTickx(0)
    c.SetTicky(0)
    c.SetGrid()
    c.cd()
    frame = c.DrawFrame(1.4,0.001, 4.1, 10)
    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.03)
    frame.GetYaxis().SetTitleOffset(1.2)
    frame.GetXaxis().SetNdivisions(508)
    frame.GetYaxis().CenterTitle(True)
    frame.GetYaxis().SetTitle("95% upper limit on #sigma / #sigma_{SM}")
    frame.GetYaxis().SetTitle(y_label_dict[plot])
    frame.GetXaxis().SetTitle(x_label)
    #frame.SetMinimum(0 if not setLogY else 0.002)
    yellow = ROOT.TGraph(2*nPoints)
    green = ROOT.TGraph(2*nPoints)
    median = ROOT.TGraph(nPoints)
    black = ROOT.TGraph(nPoints)
    #for g in [yellow,green,median]:
    #    g.GetYaxis().SetRangeUser(0 if not setLogY else 0.0002,1.)
    CMS_lumi.CMS_lumi(c,4,11)
    #CMS_lumi.CMS_lumi(c,1,1)
    window_values = outDict["central"].keys()
    window_values.sort()
    #frame.GetXaxis().SetLimits(min(window_values),max(window_values))
    frame.GetXaxis().SetLimits(0,80)
    frame.SetMinimum(0.001)
    #frame.SetMaximum(max([calculate(outDict[quan][window_value],window_value,plot) for quan in quantiles for window_value in window_values ])*maxFactor)
    frame.SetMaximum(1.E1)
    for i,window_value in enumerate(window_values):
        yellow.SetPoint( i, window_value,   calculate(outDict["up2"][window_value]         , window_value, plot) )
        yellow.SetPoint( 2*nPoints-1-i, window_value,   calculate(outDict["down2"][window_value]       , window_value, plot) )
        green.SetPoint( i, window_value,    calculate(outDict["up1"][window_value]         , window_value, plot) )
        green.SetPoint( 2*nPoints-1-i, window_value,    calculate(outDict["down1"][window_value]       , window_value, plot) )
        median.SetPoint( i, window_value,   calculate(outDict["central"][window_value]     , window_value, plot) )
        black.SetPoint( i, window_value,    calculate(outDict["obs"][window_value]         , window_value, plot))   

    mg = ROOT.TMultiGraph()
    #mg.SetMaximum(1.E3)
    #mg.SetMinimum(0.000001 if setLogY else 0.)
    #mg.GetXaxis().SetLimits(0,80)

    yellow.SetFillColor(ROOT.kOrange)
    yellow.SetLineColor(ROOT.kOrange)
    yellow.SetFillStyle(1001)
    mg.Add(yellow,'F')
    #yellow.Draw('F')

    green.SetFillColor(ROOT.kGreen+1)
    green.SetLineColor(ROOT.kGreen+1)
    green.SetFillStyle(1001)
    mg.Add(green,'F')
    #green.Draw('Fsame')

    median.SetLineColor(1)
    median.SetLineWidth(2)
    median.SetLineStyle(2)
    mg.Add(median,'L')
    #median.Draw('Lsame')

    black.SetLineColor(1)
    black.SetLineWidth(2)
    black.SetLineStyle(1)
    mg.Add(black,'L')
    #black.Draw('Lsame')

    if draw_theory:
        #xsec_graph[model].GetYaxis().SetRangeUser(0.001,0.04)
        xsec_graph[model] = make_graph(xsec,model,lambda x: x >= min(window_values) and x <= max(window_values))
        xsec_graph[model].SetLineColor(ROOT.kRed)
        xsec_graph[model].SetLineWidth(3)
        mg.Add(xsec_graph[model],'L')
        #xsec_graph[model].Draw("Lsame")
    
    #mg.GetYaxis().SetTitle(y_label_dict[plot])
    #mg.GetXaxis().SetTitle(x_label)
    #mg.Draw("a")
    mg.Draw()

    c.SaveAs(option.outputPath.replace(".pdf","_"+plot+".pdf"))    
