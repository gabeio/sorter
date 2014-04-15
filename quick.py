#!/usr/bin/env python
import subprocess
from subprocess import Popen, call

lower = "abcdefghijklmnopqrstuvwxyz"
caps = lower.upper()

for x in lower:
	#print x
	Popen(['mkdir '+x], shell=True)