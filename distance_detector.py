#!/usr/bin/env python

from gpio_module import *

#
# Lets play with ultra sound
#
class DistanceDetector (GPIO_Module):

    TRIG_PIN = 17
    ECHO_PIN = 27

    def __init__(self):
        self.setup()
        GPIO.setup(self.TRIG_PIN, GPIO.OUT)
        GPIO.setup(self.ECHO_PIN, GPIO.IN)
        GPIO.output(self.TRIG_PIN, GPIO.LOW)

    def measure(self):
        # Tigger sound pulse:
        GPIO.output(self.TRIG_PIN, True)

        # for 10 micro seconds
        time.sleep(0.00001)
        
        # stop sound pulse
        GPIO.output(self.TRIG_PIN, False)        
        
        # Now, listen/receive the pulse
        TIME_LIMIT_SEC = 1
        start = time.time()
        echo_start = -1
        echo_stop = -1

        while time.time() - start < TIME_LIMIT_SEC:
            if not GPIO.input(self.ECHO_PIN):
                echo_start = time.time()
                break

        start = time.time()
        while time.time() - start < TIME_LIMIT_SEC:
            if not GPIO.input(self.ECHO_PIN):
                echo_stop = time.time()
                break

        if echo_stop < 0 or echo_start < 0:
            return -1

        # distance = speed of sound / 2 * time diff (in centimeters)
        return (echo_stop - echo_start) * 17014

