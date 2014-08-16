#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import random

MSG="""
WARNING!!! You will destroy data on {0}.

This program erases data in 3 passes as described in
linux DoD 5220.22-M Supplement method C8.5.2.4.1

To proceed type Yes and press <Enter>
"""

def write(filename, step, func):
    print('STEP {0}'.format(step))
    with open(filename, 'w') as f:
        try:
            while 1: f.write(chr(func()))
        except IOError as e:
            pass

def three_steps(filename):
    write(filename, ' 1 - writing 0s', lambda : 0)
    write(filename, ' 2 - writing 1s', lambda : 255)
    write(filename, ' 3 - writing random', lambda : random.randint(0, 255))

if __name__ == '__main__':

    if len(sys.argv)<2:
        print("Usage:   python MediaOverwriter.py device_to_wipe")
        sys.exit(1)

    filename = sys.argv[1]

    response=raw_input(MSG.format(filename))

    if response != 'Yes':
        sys.exit(0)
    
    three_steps(filename)

