#!/usr/bin/env python

from gpio_module import *

#
# Lets observe some infrared light
#
class MotionDetector (GPIO_Module):

    PIR_PIN = 7

    def __init__(self):
        self.setup()
        GPIO.setup(self.PIR_PIN, GPIO.IN)

    def any_movement(self):
        return bool(GPIO.input(self.PIR_PIN))

    def wait_for_movement(self):
        while not self.any_movement():
            continue
        return True

