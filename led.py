#!/usr/bin/env python

from gpio_module import *

#
# Let there be light
#
class Light (GPIO_Module):

    LED_PIN = 18

    def __init__(self):
        self.setup()
        GPIO.setup(self.LED_PIN, GPIO.OUT)

    def shine(self):
        GPIO.output(self.LED_PIN, 1)

    def dark(self):
        GPIO.output(self.LED_PIN, 0)

    def shine_for(self, time_delay=0):
        self.shine()
        time.sleep(time_delay)
        self.dark()

