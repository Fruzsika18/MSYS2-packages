"""SCons.Tool.mingw_w64

Tool-specific initialization for MinGW-w64 (http://mingw-w64.sourceforge.net)

"""

#
# Copyright (c) 2015 Renato Silva
# This module is based on SCons.Tool.mingw and is licensed under the same terms
#

__revision__ = "unknown"
from SCons.Tool.mingw import *
import SCons.Tool.mingw
import SCons.Util

def find(env):
    return path if (path := env.WhereIs('gcc')) else SCons.Util.WhereIs('gcc')
