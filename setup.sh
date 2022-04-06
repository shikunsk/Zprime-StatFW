export PYTHONPATH=${PYTHONPATH}:${PWD}/
export PATH=${PATH}:${PWD}/bin/

export BASE_PATH=${PWD}

#cd /home/lucien/Higgs/DarkZ/Combine/CMSSW_8_1_0/src/ 
#eval `scramv1 runtime -sh`
#cd -

if [[ $HOSTNAME == *"lxplus"* ]] ;
then
    echo "In LXPLUS" ; 
    cd /afs/cern.ch/work/k/klo/HiggsComb/CMSSW_8_1_0/src/ ; 
elif [[ $HOSTNAME == *"ihepa"* ]] ;
then
    echo "In IHEPA" ; 
    cd /home/lucien/Higgs/DarkZ/Combine/CMSSW_8_1_0/src/ ;
elif [[ $HOSTNAME == *"ufhpc"* ]] ;
then
    echo "In UF HPG" ; 
    #cd /home/kinho.lo/Higgs/CombineArea/CMSSW_8_1_0/src/ ;
    cd /home/kshi/SUSY/CMSSW_8_0_25/src/Zprime-StatFW/CMSSW_8_1_0/src/ ;
    #cd /home/kshi/SUSY/CMSSW_8_0_25/src/Zprime-StatFW/CMSSW_10_2_13/src/ ;
fi
eval `scramv1 runtime -sh`
cd -

