#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Mcuser plugin for Varas
Author: Neon
Last modified: November 2016
"""

import urllib2
import json

desc = "Get info about a minecraft user"

def execute(par1):
	api = urllib2.urlopen("https://api.mojang.com/users/profiles/minecraft/"+par1)
	read = api.read()	
	data = json.loads(read)
	
	try:
		return "User info:\nPremium: Yes\nID: "+data["id"]
	except:
		return "User info:\nPremium: No\nID: No"
