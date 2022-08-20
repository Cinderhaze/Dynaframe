
import os

def doSomethingWithFile(file):
    print("file:%s" % file)

def doSomethingWithDir(dir):
    print("dir:%s" % dir)
    walktree(dir)


def walktree(rootFolderPath):

    for root, dirs, files in os.walk(rootFolderPath):
        for filename in files:
            doSomethingWithFile(os.path.join(root, filename))
        for dirname in dirs:
            doSomewthingWithDir(os.path.join(root, dirname)

walktree("/home/pi/Pictures/usb/Pictures")
