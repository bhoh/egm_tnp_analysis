#
# copied from AFBElectronTrigger2016_v2.py
# modified by HoOh


from HoOhElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples
samplesDef = {
    'data'   : tnpSamples.AFB['data2016_official_L1matched'].clone(),
    'mcNom'  : tnpSamples.AFB['mg2016_official_L1matched'].clone(),
    'mcAlt'  : tnpSamples.AFB['amc2016_official_L1matched'].clone(),
    'tagSel' : tnpSamples.AFB['mg2016_official_L1matched'].clone(),
}
samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
samplesDef['tagSel'].set_cut('tag_Ele_pt > 35')

baseOutDir = 'results/HoOhElectronTrigger2016_v2/'
tnpTreeDir = 'tnpEleTrig'
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.1'
additionalCutBase = {

    'Ele27_Tight94X'         : 'el_pt > 25 && passingCutBasedTight94X  == 1',
    'Ele27_Tight94XV2'       : 'el_pt > 25 && passingCutBasedTight94XV2  == 1',
    'Ele27_MVA94Xwp90iso'    : 'el_pt > 25 && passingMVA94Xwp90iso == 1',
    'Ele27_MVA94Xwp90isoV2'  : 'el_pt > 25 && passingMVA94Xwp90isoV2 == 1',
}
flags = {
    'Ele27_Tight94X'         : '(passHltEle27WPTightGsf == 1)',
    'Ele27_Tight94XV2'       : '(passHltEle27WPTightGsf == 1)',
    'Ele27_MVA94Xwp90iso'    : '(passHltEle27WPTightGsf == 1)',
    'Ele27_MVA94Xwp90isoV2'  : '(passHltEle27WPTightGsf == 1)',
}
