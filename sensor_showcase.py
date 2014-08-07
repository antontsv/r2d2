#!/usr/bin/env python

import argparse
from motion_detector import *
from led import *
from distance_detector import *


parser = argparse.ArgumentParser(description='Sensor showcase')
parser.add_argument('-a','--all', action="store_true", help='Show all demos')
parser.add_argument('-m','--motion', action="store_true", help='Motion sensor demo')
parser.add_argument('-l','--led', action="store_true", help=u'Led demo')
parser.add_argument('-d','--distance', action="store_true", help=u'Led demo')
args = parser.parse_args()

def header(title='Some demo'):
    char = '*'
    frame = char * (len(title) + 4)
    print frame
    print "%s %s %s" % (char,title,char)
    print frame

print "Press CTRL+C to quit at any time"
DEMO_RUNTIME_SEC = 30

if args.all or args.motion:

    header("Motion sensor demo")
    print "Will be moving to next demo in %d seconds" % DEMO_RUNTIME_SEC
    print "Wave or walk in front of connected PIR sensor. You should see message once motion is detected."
    start = time.time()
    md = MotionDetector()

    i=0
    while time.time() - start < DEMO_RUNTIME_SEC:
        if md.any_movement():
            i+=1
            print "Motion Detected - %d" % i
            print '...zzz'
            time.sleep(0.5)

if args.all or args.led:

    header("LED light demo")
    print "Will be moving to next demo in %d seconds" % DEMO_RUNTIME_SEC
    start = time.time()
    led = Light()
    LIGHT_TIME_SEC = 5
    SLEEP_TIME_SEC = 3

    while time.time() - start < DEMO_RUNTIME_SEC:
        print "Shining for %d seconds..." % LIGHT_TIME_SEC
        led.shine_for(LIGHT_TIME_SEC)
        print '...zzz'
        time.sleep(SLEEP_TIME_SEC)


if args.all or args.distance:

    header("Distance detector demo")
    print "Will be moving to next demo in %d seconds" % DEMO_RUNTIME_SEC
    detector = DistanceDetector()
    start = time.time()
    INTERVAL_SEC = 3

    while time.time() - start < DEMO_RUNTIME_SEC:
        pos = 0
        false_count = 0
        collective = 0
        current_measure_start=time.time()
        while time.time() - current_measure_start < INTERVAL_SEC:
            reading = detector.measure()
            if reading > 0:
                pos += 1
                collective += reading
            else:
                false_count += 1
        print "Distance measured over interval of %d sec: %f cm (pos: %d, false: %d)" % (INTERVAL_SEC, collective/pos, pos, false_count)
