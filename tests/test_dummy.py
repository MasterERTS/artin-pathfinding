# -*- coding: utf-8 -*-

'''
@author : Erwin Lejeune <erwin.lejeune15@gmail.com>
@date : 28/01/2020
@brief : dummy test file
'''

import numpy as np
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from lib.world import World
from lib.pathfinder import *

def test_dummy():
    y = 2
    y -= 2
    assert(y == 0)