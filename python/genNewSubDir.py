#!usr/bin python
#a simple script for createing user subdirectory to act as physical website location.
import os
import sys
path="" #this needs to be defined so the code currently won't run
cont = True
try:
	os.mkdir(path+sys.argv[1])
except OSError:
	cont=False
	print("oops we have experienced a problem") #more helpful error report is probably needed


