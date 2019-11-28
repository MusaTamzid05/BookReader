import os

TEMP_PATH = "/tmp/test.wav"

def speak(sentence , print_sentence = True):

    if print_sentence:
        print("*" * 30)
        print(sentence)
        print("*" * 30)

    commands = [
            "pico2wave -w={} '{}'".format(TEMP_PATH , sentence),
            "aplay {}".format(TEMP_PATH),
            "rm {}".format(TEMP_PATH)
            ]

    for command in commands:
        if os.system(command) != 0:
            return False


    return True
