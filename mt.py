#!/usr/bin/env python
import sys
mt = 69
if len(sys.argv) > 1 and sys.argv[1].isdigit():
	mt = int(sys.argv[1])
for i in range(mt):
	print "Mmmm... Toasty"
