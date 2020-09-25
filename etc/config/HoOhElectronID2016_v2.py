# copied from AFBElectronID2016_v2.py
# and modified by HoOh
#
from HoOhElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples

# flag to be Tested

samplesDef = {
    'data'   : tnpSamples.AFB['data2016_official'].clone(),
    'mcNom'  : tnpSamples.AFB['mg2016_official'].clone(),
    'mcAlt'  : tnpSamples.AFB['amc2016_official'].clone(),
    'tagSel' : tnpSamples.AFB['mg2016_official'].clone(),
}
samplesDef["mcNom"].set_cut(tight_mcTrue)
samplesDef['mcAlt'].set_cut(tight_mcTrue)
samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
samplesDef['tagSel'].set_cut('tag_Ele_pt > 35 && '+tight_mcTrue)

baseOutDir = 'results/HoOhElectronID2016_v2/'
tnpTreeDir = 'tnpEleIDs'
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.1'
additionalCutBase = {
    'noAdditionalCut' : '1',
}
flags = {
    'Tight94X'  : '(passingCutBasedTight94X  == 1)',
    'Tight94XV2'  : '(passingCutBasedTight94XV2  == 1)',
    'MVA94Xwp90iso'  : '(passingMVA94Xwp90iso == 1)',
    'MVA94Xwp90isoV2'  : '(passingMVA94Xwp90isoV2 == 1)',
}
