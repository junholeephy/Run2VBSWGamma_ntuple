from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'STtw-1'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['Summer16_23Sep2016V3_MC_L1FastJet_AK4PFchs.txt','Summer16_23Sep2016V3_MC_L2Relative_AK4PFchs.txt','Summer16_23Sep2016V3_MC_L3Absolute_AK4PFchs.txt','Summer16_23Sep2016V3_MC_L1FastJet_AK4PFPuppi.txt','Summer16_23Sep2016V3_MC_L2Relative_AK4PFPuppi.txt','Summer16_23Sep2016V3_MC_L3Absolute_AK4PFPuppi.txt']
# Name of the CMSSW configuration file
config.JobType.psetName    = 'analysis.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'STtw-1'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'  #2_CH_CERN'



