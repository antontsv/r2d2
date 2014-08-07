#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import atexit

# Save system's current exception hook
excepthook = sys.excepthook

#
# Generic behaviour
#
class GPIO_Module(object):

    SHOW_GPIO_WARNINGS = False
    
    initialized = False

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(self.SHOW_GPIO_WARNINGS)
        self.initialized = True

    @staticmethod
    def onException(type, value, traceback):
        # Ignore keyboard interrupt, but report other exceptions
        if type != KeyboardInterrupt:       
            excepthook(type, value, traceback)
        else:
            print 'Received keyboard interrupt. Exiting now...'

    @staticmethod
    def cleanup():
        try:
            if GPIO_Module.initialized:
                sys.stdout.write('Cleaning up GPIO...')
                GPIO.cleanup()
                print 'done'
        except Exception, e:
            print 'failed'
    
#
# Some time exit hooks:
#
sys.excepthook = GPIO_Module.onException
atexit.register(GPIO_Module.cleanup)
