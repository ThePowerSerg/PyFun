#!/usr/bin/env python3

import sys
import subprocess

#get file name from command line argument
with open(sys.argv[1], 'r') as f:
    #create a list of lines from the file and remove white spaces
    lines = [line.strip() for line in f]
    #iterate through lines and perform name change
    for line in lines:
        newline = line.replace("jane", "jdoe")
        #used for testing purposes
        #print("mv", ".."+line, ".."+newline)
        #run the process, must be passed as a list
        subprocess.run(["mv", ".."+line, ".."+newline])
f.close()