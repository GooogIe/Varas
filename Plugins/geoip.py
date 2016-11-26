#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Geoip plugin for Varas
Author: Neon
Last modified: November 2016
"""
import urllib2

desc = "Attempt to retrieve infos about a provided IP"

def execute(par1):
	api = urllib2.urlopen("http://api.predator.wtf/geoip/?arguments="+par1)
	read = api.read()
	rtr = read.replace("<br>", "\n",100)
	return rtr
