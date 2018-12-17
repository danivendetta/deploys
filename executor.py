#!/usr/bin/python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------
# Nom:            deploy.py
# Purpose:      deploys automatics.
#
# Creacio:      05 de December 2018
# Copyright:    (c) 2007 per DAI.
# Llicència:    GNU GENERAL PUBLIC LICENSE Version 3
# Versió:       0.1
#----------------------------------------------------------------------------
#
# deploy.py is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# deploy.py is distrubuted in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with BackupCfg; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

import os, stat, time
import gzip
import shutil
from optparse import OptionParser,  make_option
import re

def lista_sites():
