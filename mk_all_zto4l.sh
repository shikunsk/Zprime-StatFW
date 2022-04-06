#!/bin/bash

#inputDir=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2016/2020-11-06/
#inputDir=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2017/2020-11-06/
#inputDir=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2018/2020-11-06/
#inputDir=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2016_Run2017/2020-11-06/
#inputDir2016=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2016/2020-11-06/
#inputDir2017=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2017/2020-11-06/
#inputDir2018=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2018/2020-11-06/
inputDir2016=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2016/2022-03-06_ULdata/
inputDir2017=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2017/2022-03-06_ULdata/
inputDir2018=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2018/2022-03-06_ULdata/
#inputDir2016=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2016/2021-11-09/
#inputDir2017=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2017/2021-11-09/
#inputDir2018=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2018/2021-11-09/
#inputDir2016=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2016/2020-11-23_coup0.05/
#inputDir2017=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2017/2020-11-23_coup0.05/
#inputDir2018=/cmsuf/data/store/user/t2/users/kshi/data_ihepa/Zprime/Zto4l/ParaInput/Run2018/2020-11-23_coup0.05/


#outputDir=DataCard_Zto4l/Run2016/2020-11-06/Zprime/
#shiyan=DataCard_Zto4l/Run2016/2020-11-06/Zprime/result
#limit_xs=DataCard_Zto4l/Run2016/2020-11-06/Zprime/limit_xs
#coupling=DataCard_Zto4l/Run2016/2020-11-06/Zprime/coupling
#outputDir=DataCard_Zto4l/Run2017/2020-11-06/Zprime/
#shiyan=DataCard_Zto4l/Run2017/2020-11-06/Zprime/result
#limit_xs=DataCard_Zto4l/Run2017/2020-11-06/Zprime/limit_xs
#coupling=DataCard_Zto4l/Run2017/2020-11-06/Zprime/coupling
#outputDir=DataCard_Zto4l/Run2018/2020-11-06/Zprime/
#shiyan=DataCard_Zto4l/Run2018/2020-11-06/Zprime/result
#limit_xs=DataCard_Zto4l/Run2018/2020-11-06/Zprime/limit_xs
#coupling=DataCard_Zto4l/Run2018/2020-11-06/Zprime/coupling
#outputDir=DataCard_Zto4l/EXO/2020-11-06/Zprime/
#shiyan=DataCard_Zto4l/EXO/2020-11-06/Zprime/result
#limit_xs=DataCard_Zto4l/EXO/2020-11-06/Zprime/limit_xs
#coupling=DataCard_Zto4l/EXO/2020-11-06/Zprime/coupling
#outputDir=DataCard_Zto4l/EXO/2020-11-24_fit/Zprime/
#shiyan=DataCard_Zto4l/EXO/2020-11-24_fit/Zprime/result
#limit_xs=DataCard_Zto4l/EXO/2020-11-24_fit/Zprime/limit_xs
#coupling=DataCard_Zto4l/EXO/2020-11-24_fit/Zprime/coupling
#outputDir=DataCard_Zto4l/EXO/2021-10-14_Compare/Zprime/
#shiyan=DataCard_Zto4l/EXO/2021-10-14_Compare/Zprime/result
#limit_xs=DataCard_Zto4l/EXO/2021-10-14_Compare/Zprime/limit_xs
#coupling=DataCard_Zto4l/EXO/2021-10-14_Compare/Zprime/coupling
#outputDir=DataCard_Zto4l/EXO/2021-11-09_newstat/Zprime/
#shiyan=DataCard_Zto4l/EXO/2021-11-09_newstat/Zprime/result
#limit_xs=DataCard_Zto4l/EXO/2021-11-09_newstat/Zprime/limit_xs
#coupling=DataCard_Zto4l/EXO/2021-11-09_newstat/Zprime/coupling
#outputDir=DataCard_Zto4l/Run2018/2021-11-29/Zprime/
#shiyan=DataCard_Zto4l/Run2018/2021-11-29/Zprime/result
#limit_xs=DataCard_Zto4l/Run2018/2021-11-29/Zprime/limit_xs
#coupling=DataCard_Zto4l/Run2018/2021-11-29/Zprime/coupling
#outputDir=DataCard_Zto4l/EXO/2022-03-06_ULdata/Zprime/
#shiyan=DataCard_Zto4l/EXO/2022-03-06_ULdata/Zprime/result
#limit_xs=DataCard_Zto4l/EXO/2022-03-06_ULdata/Zprime/limit_xs
#coupling=DataCard_Zto4l/EXO/2022-03-06_ULdata/Zprime/coupling
#outputDir=DataCard_Zto4l/EXO/compare_test/Zprime/
#shiyan=DataCard_Zto4l/EXO/compare_test/Zprime/result
#limit_xs=DataCard_Zto4l/EXO/compare_test/Zprime/limit_xs
#coupling=DataCard_Zto4l/EXO/compare_test/Zprime/coupling



#outputDir=DataCard_Zto4l/RunII/2020-11-06/Zprime/
#shiyan=DataCard_Zto4l/RunII/2020-11-06/Zprime/result
#limit_xs=DataCard_Zto4l/RunII/2020-11-06/Zprime/limit_xs
#coupling=DataCard_Zto4l/RunII/2020-11-06/Zprime/coupling
#outputDir=DataCard_Zto4l/RunII/2020-11-23_coup0.05/Zprime/
#shiyan=DataCard_Zto4l/RunII/2020-11-23_coup0.05/Zprime/result
#limit_xs=DataCard_Zto4l/RunII/2020-11-23_coup0.05/Zprime/limit_xs
#coupling=DataCard_Zto4l/RunII/2020-11-23_coup0.05/Zprime/coupling
#outputDir=DataCard_Zto4l/RunII/2020-11-24_fit_coup0.05/Zprime/
#shiyan=DataCard_Zto4l/RunII/2020-11-24_fit_coup0.05/Zprime/result
#limit_xs=DataCard_Zto4l/RunII/2020-11-24_fit_coup0.05/Zprime/limit_xs
#coupling=DataCard_Zto4l/RunII/2020-11-24_fit_coup0.05/Zprime/coupling
#outputDir=DataCard_Zto4l/RunII/test/Zprime/
#shiyan=DataCard_Zto4l/RunII/test/Zprime/result
#limit_xs=DataCard_Zto4l/RunII/test/Zprime/limit_xs
#coupling=DataCard_Zto4l/RunII/test/Zprime/coupling
#outputDir=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/
#shiyan=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/result
#limit_xs=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/limit_xs
#coupling=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/coupling
#outputDir=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/
#shiyan=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/result1
#limit_xs=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/limit_xs1
#coupling=DataCard_Zto4l/RunII/2021-09-28_Dissertation/Zprime/coupling1
#outputDir=DataCard_Zto4l/RunII/2022-03-06_ULdata/Zprime/
#shiyan=DataCard_Zto4l/RunII/2022-03-06_ULdata/Zprime/result
#limit_xs=DataCard_Zto4l/RunII/2022-03-06_ULdata/Zprime/limit_xs
#coupling=DataCard_Zto4l/RunII/2022-03-06_ULdata/Zprime/coupling
outputDir=DataCard_Zto4l/RunII/2022-03-23_ULdata/Zprime/
shiyan=DataCard_Zto4l/RunII/2022-03-23_ULdata/Zprime/result
limit_xs=DataCard_Zto4l/RunII/2022-03-23_ULdata/Zprime/limit_xs
coupling=DataCard_Zto4l/RunII/2022-03-23_ULdata/Zprime/coupling

#outputDir=DataCard_Zto4l/Run1718/2020-11-06/Zprime/
#shiyan=DataCard_Zto4l/Run1718/2020-11-06/Zprime/result
#limit_xs=DataCard_Zto4l/Run1718/2020-11-06/Zprime/limit_xs
#coupling=DataCard_Zto4l/Run1718/2020-11-06/Zprime/coupling


#python makeDataCard_zto4l.py --inputDir=${inputDir} --outputDir ${outputDir} --verbose
#python makeDataCard_zto4l.py --inputDir=${inputDir2016} --outputDir ${outputDir} --appendToPath "2016" --verbose
#python makeDataCard_zto4l.py --inputDir=${inputDir2017} --outputDir ${outputDir} --appendToPath "2017" --verbose
#python makeDataCard_zto4l.py --inputDir=${inputDir2018} --outputDir ${outputDir} --appendToPath "2018" --verbose


#for d in $(ls ${outputDir}); 
#do
    #python makeWorkspace1.py --inputDir ${outputDir}/${d}/ --cardName ${d}.txt --combinePattern "ZpToMuMu_M*.txt" #--pattern "ZpToMuMu_M*.txt" 
#done

#python runCombineTask.py --inputDir ${outputDir} --selectStr "ZpToMuMu_M*" --option "--minosAlgo bisection" #stepping" #bisection" #"-t -1 --run=blind"

#python plotLimit_xs.py --inputDir ${outputDir} --outputPath ${shiyan}
#python plotLimit_xs.py --inputDir ${outputDir} --outputPath ${limit_xs}
python plotLimit_xs.py --inputDir ${outputDir} --outputPath ${coupling}
