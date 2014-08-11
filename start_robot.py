#!/usr/bin/env python

import argparse
from motion_detector import *
from led import *
from distance_detector import *
from sound_manager import *


class R2D2:
    
    def __init__(self):
        self.motion_detector = MotionDetector()
        self.led = Light()
        self.distance_detector = DistanceDetector()
        self.sound_manager = SoundManager()

    def run(self):
        print "R2D2: started and operating"
        while True:
            self.motion_detector.wait_for_movement()
            self.led.shine()
            print "Measuring distance"
            distance = self.distance_detector.distance_over_time(3)
            if(distance > 0 and distance < 100):
                print "Something is close by (%d cm), lets do something..." % distance
                self.sound_manager.play_next()
            else:
                print "Object is too far: %d cm" % distance
            self.led.dark()



robot = R2D2()
robot.run()
