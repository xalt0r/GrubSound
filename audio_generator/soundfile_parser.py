#! /usr/bin/env python3

"""
Grub soundfile syntax:
    tempo [pitch1 duration1] [pitch2 duration2]...

tempo: 32b little-endian, unsigned
    - measured as bpm
    - 60 --> 1s base duration
    - 120 -> 0.5s base duration
pitch/duration: 16b little-endian, unsigned
    - measured in Hz
    - pitch of 0Hz gives a rest
"""

TEMPO = 0
NOTES = []

"""
"""
def parse_file(file_name: string):
    with open(file_name, "r") as file:
        NOTES = file.read().split()

    TEMPO = NOTES.pop(0)

