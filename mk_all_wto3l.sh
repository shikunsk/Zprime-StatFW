#!/bin/bash

#inputDir=/raid/raid7/lucien/Higgs/Zprime/ParaInput/EXO-18-001-Nominal/2019-06-05/
#outputDir=DataCard/EXO-18-001-Nominal/2019-06-05/

inputDir=/raid/raid7/kshi/Zprime/Wto3l/ParaInput/Run2016/2019-08-27/
#outputDir=DataCard/2019-08-27/mass2/300Mev/
outputDir=DataCard/2020-01-22/mass2/300Mev/
shiyan=DataCard/2020-01-22/mass2/300Mev/result

#python makeDataCard_wto3l.py --inputDir=${inputDir} --outputDir ${outputDir} --verbose

#for d in $(ls ${outputDir}); 
#do
    #python makeWorkspace.py --inputDir ${outputDir}/${d}/ --pattern "WTo3munu_ZpM*.txt"
#done

#python runCombineTask.py --inputDir ${outputDir} --selectStr "WTo3munu_ZpM*" --option "-t -1 --run=blind"

python plotLimit.py --inputDir ${outputDir} --outputPath ${shiyan}
