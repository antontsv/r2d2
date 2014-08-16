#!/usr/bin/env python

import daemon
from r2d2 import *


with daemon.DaemonContext():
    robot = R2D2()
    robot.run()
