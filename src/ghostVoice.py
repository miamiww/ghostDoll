#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import random
import serial
import os
import threading

fortunes = ['you will not  make it home in time','your death will be painful and in your final moments you will know that you deserved it' ,'you will die tomorrow','stop sleeping or it will find you','be careful when walking, perhaps avoid walking altogether','your right index finger will be cut off at the second knuckle two months and two days from today','you will live to a contented old age but no one will remember you within ten years of your passing' ]
ser = serial.Serial('/dev/ttyACM0',9600)



def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('Fortune')
    recognizer.expect_phrase('future')
    recognizer.expect_phrase('life')

    os.system('aplay soloKnocks.wav')
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('ready for knock')
#        aiy.audio.say('Hello')
        while True:
            os.system('aplay soloKnocks.wav')
            reading = ser.read(1)
            if reading == '!':
                break
#        ser.write(b'?')
        print('Listening...')
        aiy.audio.say('ask me for your future')

        text = recognizer.recognize()
        if text is None:
            aiy.audio.say('please speak')
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'turn on the light' in text:
                led.set_state(aiy.voicehat.LED.ON)
                ser.write(b'?')
            elif 'turn off the light' in text:
                led.set_state(aiy.voicehat.LED.OFF)
#            elif 'blink' in text:
#                led.set_state(aiy.voicehat.LED.BLINK)
            elif 'future' in text:
                aiy.audio.say(random.choice(fortunes))
                ser.write(b'?')
            elif 'Fortune' in text:
                aiy.audio.say('beware your family')
                ser.write(b'?')
            elif 'goodbye' in text:
                break


if __name__ == '__main__':
    main()
