#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Updater Module for Varas

Author: Neon

Last modified: November 2016
"""

import urllib2
import os
import sys
import time
#Don't write bytecodes file (.pyc)
sys.dont_write_bytecode = True

defcol = "\033[0m"
red="\033[1;31m"
green="\033[1;32m"

#Check for updates
def check(current):
	try:
		update = urllib2.urlopen("https://raw.githubusercontent.com/neon-loled/varas-update/master/update.txt")#Temporary url
		read = update.read()
		if(str(current) in str(read)):
			return True
		else:
			return False
	except:
		return False
	
#Updater function
def update():
		bot = urllib2.urlopen("https://raw.githubusercontent.com/GooogIe/Varas/master/Bot.py")
		bot = bot.read()
		utils = urllib2.urlopen("https://raw.githubusercontent.com/GooogIe/Varas/master/Utils.py")
		utils = utils.read()
		botf = open("Bot.py","w")
		botf.write(bot)
		botf.close()
		print red+"["+green+"+"+red+"] - "+defcol+"Bot.py overwritten."
		utilsf = open("Utils.py","w")
		utilsf.write(utils)
		utilsf.close()
		print red+"["+green+"+"+red+"] - "+defcol+"Utils.py overwritten."
		print red+"["+green+"-"+red+"] - "+defcol+"Quitting..."
		time.sleep(1)
		os.system("pkill python")
