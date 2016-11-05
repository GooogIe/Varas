#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Help plugin for Vars

Author: Habb0n

Last modified: November 2016


Github: https://github.com/GooogIe
"""

import os
from os import listdir
from os.path import isfile, join

desc = "Simple command that let you see all the bot plugins."

if os.name == 'nt':
	plugindir = os.getcwd()+"\Plugins"
else:
	plugindir = os.getcwd()+"/Plugins"

def execute():
	help= [f for f in listdir(plugindir) if isfile(join(plugindir, f))]
	i = 0
	while i < len(help):
		if ".pyc" in help[i] or "__init__" in help[i]:
			del help[i]
		else:
			help[i] = help[i].replace(".py","")
			if help[i] != "help":
				exec("import "+help[i])
				exec("dc = "+help[i]+".desc")
			else:
				dc = desc
			help[i] = help[i]+" - "+dc
			i +=1
	help.sort()
	return "Available Commands: \n"+"\n".join(help)
