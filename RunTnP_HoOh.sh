#!/bin/bash

#    'Tight94X'  : '(passingCutBasedTight94X  == 1)',
#    'Tight94XV2'  : '(passingCutBasedTight94XV2  == 1)',
#    'MVA94Xwp90iso'  : '(passingMVA94Xwp90iso == 1)',
#    'MVA94Xwp90isoV2'  : '(passingMVA94Xwp90isoV2 == 1)',


python tnpEGM_fitter.py etc/config/HoOhElectronID2016_v2.py --flag Tight94XV2 --createBins
python tnpEGM_fitter.py etc/config/HoOhElectronID2016_v2.py --flag Tight94XV2 --createHists -n 30
python tnpEGM_fitter.py etc/config/HoOhElectronID2016_v2.py --flag Tight94XV2 --doFit -n 30
