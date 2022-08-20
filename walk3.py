import os
import pprint
pp = pprint.PrettyPrinter()

dir = "/home/pi/Pictures/usb/Pictures"
extensions = ['.mp4', '.mov', '.jpg']

files = [os.path.join(path, filename)
         for path, dirs, files in os.walk(dir)
         for filename in files
         if os.path.splitext(filename)[1] in extensions
        ]

pp.pprint(files)
#return random.choice(files)
