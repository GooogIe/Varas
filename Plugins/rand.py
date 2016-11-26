
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Random plugin for Varas
Author: Neon
Last modified: November 2016
"""

import random

desc = "Generate a random Integer (range)"

def execute(par1, par2):
	par1 = int(par1)
	par2 = int(par2)
	rand = random.randint(par1,par2)
	return str(rand)
