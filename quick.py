#!/usr/bin/env python
import subprocess
from subprocess import Popen, call

lower = "abcdefghijklmnopqrstuvwxyz"
caps = lower.upper()

for x in lower:
	Popen(['mkdir '+x,], shell=True)
	Popen(['mv '+x+'*.* ./'+x], shell=True)

for x in upper:
	Popen(['mv '+x+'*.* ./'+x], shell=True)