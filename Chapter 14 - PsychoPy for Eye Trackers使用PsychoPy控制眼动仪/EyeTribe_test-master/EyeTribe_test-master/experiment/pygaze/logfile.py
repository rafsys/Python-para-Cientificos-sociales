# -*- coding: utf-8 -*-
#
# This file is part of PyGaze - the open-source toolbox for eye tracking
#
#	PyGaze is a Python module for easily creating gaze contingent experiments
#	or other software (as well as non-gaze contingent experiments/software)
#	Copyright (C) 2012-2013  Edwin S. Dalmaijer
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>

from pygaze.defaults import *
try:
	from constants import *
except:
	pass

from pygaze._misc.misc import copy_docstr
from pygaze._logfile.baselogfile import BaseLogfile

class Logfile(BaseLogfile):

	# See BaseLogfile

	def __init__(self, **args):

		# See BaseLogfile

		from pygaze._logfile.logfile import Logfile
		self.__class__ = Logfile
		self.__class__.__init__(self, **args)
		copy_docstr(BaseLogfile, Logfile)
