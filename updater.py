#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Updater module

Author: Neon

Last modified: November 2016
"""


import urllib2
import os
import sys

#Don't write bytecodes file (.pyc)
sys.dont_write_bytecode = True


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
		utilsf = open("Utils.py","w")
		utilsf.write(utils)
		utilsf.close
		os.system("pkill python")
