#!/usr/bin/python3
import os
import sys
name = sys.argv[1]
if sys.argv == 3:
    template = sys.argv[2]
else:
    template = "standard"
os.system(f"cp /opt/mytools/gentemplate/templates/{template}.txt {name}.py")
