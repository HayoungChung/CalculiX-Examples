#!/usr/bin/python
import os

os.system("param.py par.pre.fbd")
os.system("cgx -b pre.fbd")
os.system("ccx solve")
os.system("monitor.py solve")
os.system("cgx -b post.fbd")


