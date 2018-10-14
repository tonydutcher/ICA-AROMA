#!/usr/bin/env python

import os
import sys
import numpy as np

aromadir = sys.argv[1]
motion_ics = np.loadtxt(os.path.join(aromadir, 'classified_motion_ICs.txt'),
                        delimiter=',', dtype=int) - 1
mix = np.loadtxt(os.path.join(aromadir, 'melodic.ica', 'melodic_mix'))
np.savetxt(os.path.join(aromadir, 'confound.txt'), mix[:,motion_ics])
