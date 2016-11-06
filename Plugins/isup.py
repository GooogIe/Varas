#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Isup plugin for Varas
Author: Neon
Last modified: November 2016
"""

import urllib2

desc = "Check if a website is up or not"

def execute(url):
	api = urllib2.urlopen("http://isup.me/"+url)
	read = api.read()
	
	if "It's not just you!" in read:
		return url + " is offline."
	elif "It's just you" in read:
		return url+ " is online."
	else:
		return "An error has occured."
