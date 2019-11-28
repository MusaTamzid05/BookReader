import os

def speak(sentence):

    commands = [
            "pico2wave -w=/tmp/test.wav '{}'".format(sentence),
            "aplay /tmp/test.wav",
            "rm /tmp/test.wav"
            ]


    for command in commands:
        os.system(command)
