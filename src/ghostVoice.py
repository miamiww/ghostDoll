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

fortunes = ['there are no weddings in your future','you will burn your mouth on a bowl of soup within the next 728 hours','your next job will be your last. maybe wait a while in the job you have now','on January 19th, 2018 you will mysteriously lose consciousness. this will be the first of what will become a regular occurence','I do not see anything interesting in your future. guess you must be pretty boring','in three days you will be walking down a dark hallway and stub your toe','serious trouble will find you','a family member will betray you','you will not  make it home in time','in your final moments you will know that you deserved it' ,'you will die tomorrow','bad things will happen to you when walking. be careful when walking, perhaps avoid walking altogether','your right index finger will be cut off at the second knuckle two months and two days from today','you will live to a contented old age', 'you will have an unfortunate accident when shaking the hand of a stranger' ]
fortunes.append('your next flight will be your last')
chitChat = ['that was my name when I was living']
ser = serial.Serial('/dev/ttyACM0',9600)



def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('Fortune')
    recognizer.expect_phrase('hello')
    recognizer.expect_phrase('future')
    recognizer.expect_phrase('life')
    recognizer.expect_phrase('Sophia')
    recognizer.expect_phrase('tell me my fortune')
    recognizer.expect_phrase('close the panel')
    recognizer.expect_phrase('go away')
    recognizer.expect_phrase('when')
    recognizer.expect_phrase('how many')
    recognizer.expect_phrase('will I')


    os.system('aplay soloKnocks.wav')
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('ready for knock')
#        aiy.audio.say('Hello')
#        while True:
#            os.system('aplay soloKnocks.wav')
#            reading = ser.read(1)
#            if reading == '!':
#                break
#        ser.write(b'?')
        reading = ser.read(1)
        print('Listening...')
        aiy.audio.say('ask me for your future')

        text = recognizer.recognize()
        if text is None:
            aiy.audio.say('please speak')
            print('Sorry, I did not hear you.')
            ser.write(b'?')
            ser.flush()
        else:
            print('You said "', text, '"')
            if 'turn on the light' in text:
                led.set_state(aiy.voicehat.LED.ON)
                ser.write(b'?')
                ser.flush()
            elif 'turn off the light' in text:
                led.set_state(aiy.voicehat.LED.OFF)
                ser.write(b'?')
#            elif 'blink' in text:
#                led.set_state(aiy.voicehat.LED.BLINK)
            elif 'hello' in text:
                aiy.audio.say('hello')
                ser.write(b'?')
                ser.flush()
            elif 'future' in text:
                aiy.audio.say(random.choice(fortunes))
                ser.write(b'?')
                ser.flush()
            elif 'when' in text:
                aiy.audio.say('tomorrow')
                ser.write(b'?')
            elif 'my fortune' in text:
                aiy.audio.say(random.choice(fortunes))
                ser.write(b'?')
                ser.flush()
            elif '4chan' in text:
                aiy.audio.say(random.choice(fortunes))
                ser.write(b'?')
                ser.flush()
            elif 'Sophia' in text:
                aiy.audio.say(random.choice(chitChat))
                ser.write(b'?')
                ser.flush()
            elif 'close the panel' in text:
                aiy.audio.say('okay')
                ser.write(b'?')
                ser.flush()
            elif 'will I' in text:
                aiy.audio.say('no')
                ser.write(b'?')
                ser.flush()
            elif 'how many' in text:
                aiy.audio.say('zero')
                ser.write(b'?')
                ser.flush
#            elif 'goodbye' in text:
#                break
            elif 'go away' in text:
                ser.write(b'?')
                ser.flush()
            else:
                aiy.audio.say('you do not want to know')
                ser.write(b'?')
                ser.flush()


if __name__ == '__main__':
    main()
