#!/usr/bin/python

import os

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("/home/pi/Pictures/usb/Pictures"):
    path = root.split(os.sep)
    print(path)
    #print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)
