#!/bin/bash

inputDir=/raid/raid7/lucien/Higgs/Zprime/ParaInput/EXO-18-001-Nominal/2019-06-05/
outputDir=DataCard/EXO-18-001-Nominal/2019-06-05/

python makeDataCard.py --inputDir=/raid/raid7/lucien/Higgs/Zprime/ParaInput/EXO-18-001-Nominal/2019-06-05/ --outputDir DataCard/EXO-18-001-Nominal/2019-06-05/ --verbose

for d in $(ls ${outputDir}); 
do
    python makeWorkspace.py --inputDir ${outputDir}/${d}/ --pattern "ZpToMuMu_M*.txt"
done

python runCombineTask.py --inputDir ${outputDir} --selectStr "ZpToMuMu_M" --option "-t -1 --run=blind"
