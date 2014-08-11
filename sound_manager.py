#!/usr/bin/env python

import sys
import os
import time
import random
import alsaaudio
import pyttsx
from subprocess import call

#
# Our sound coordinator
#
class SoundManager ():

    SOUND_PLAYER   = 'mpg123'
    SOUNDS_DIR     = 'sounds'
    SOUND_FILE_EXT = 'mp3'

    sound_list = []
    next_in_queue = []

    def __init__(self):
        self.requires(self.SOUND_PLAYER)
        self.mixer = alsaaudio.Mixer('PCM')
        self.speech_engine = pyttsx.init()
        ext = ".%s" % self.SOUND_FILE_EXT
        for dirpath, dirnames, filenames in os.walk(self.SOUNDS_DIR):
            for filename in filenames:
                if filename.endswith(ext):
                    full_path = os.path.join(dirpath, filename)
                    self.sound_list.append(full_path)

    @staticmethod
    def requires(utility):
        devnull = open(os.devnull, 'w')
        if call(['which', utility], stdout=devnull, stderr=devnull) != 0:
            print "Sound manager requires '%s' utility" % utility
            devnull.close()
            sys.exit(1)
        else: 
            devnull.close()

    def play(self, filepath):
        devnull = open(os.devnull, 'w')
        ret = call([self.SOUND_PLAYER, filepath], stdout=devnull, stderr=devnull)
        devnull.close()
        return ret == 0

    def play_random(self):
        l = len(self.sound_list)
        if l > 0:
            return self.play(self.sound_list[random.randint(0,l-1)])
        else:
            return False

    def play_next(self):
        if len(self.next_in_queue) <= 0:
            l = len(self.sound_list)
            if l > 0:
                self.next_in_queue = range(0,l)
                random.shuffle(self.next_in_queue)
            else:
                return False
        sound_position_id = self.next_in_queue.pop()
        return self.play(self.sound_list[sound_position_id])

    def say(self, text):
        self.speech_engine.say(text)
        self.speech_engine.runAndWait() 

    def mute(self):
        self.mixer.setmute(1)

    def unmute(self):
        self.mixer.setmute(0)
