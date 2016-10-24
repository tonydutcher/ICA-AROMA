#!/usr/bin/env python

import os
import sys
import numpy as np

from mvpa2.misc.fsl.base import FslGLMDesign, read_fsl_design

icafile = sys.argv[1]
matfile = sys.argv[2]
outfile = sys.argv[3]
regs = np.fromstring(sys.argv[4], sep=',', dtype=int) - 1

desmat = FslGLMDesign(matfile)
icamat = np.loadtxt(icafile)
fullmat = np.hstack((icamat, desmat.mat[:,regs]))

np.savetxt(outfile, fullmat)
