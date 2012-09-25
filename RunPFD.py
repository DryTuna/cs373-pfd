#!/usr/bin/env python

"""
To run the program
% python RunPFD.py < RunPFD.in > RunPFD.out
% chmod ugo+x RunPFD.py
% RunPFD.py < RunPFD.in > RunPFD.out

To document the program
% pydoc -w PFD
"""

# -------
# imports
# -------

import sys

from PFD import pfd_start

# ----
# main
# ----

pfd_start(sys.stdin, sys.stdout)
