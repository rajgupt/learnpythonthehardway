from sys import argv
import os

filename = raw_input("enter file name: ")

if not os.path.exists(filename):
    print "file is invalid"
else:

    print "file name is: %r " % filename
    fid = open(filename)
    print fid.read()
