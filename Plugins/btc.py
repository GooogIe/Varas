#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Isup plugin for Varas
Author: Neon
Last modified: November 2016
"""
import urllib2

desc = "Return current balance from a Bitcoin wallet"

def execute(par1):
	#1btc = 100000000satoshi
	api = urllib2.urlopen("https://blockchain.info/it/q/addressbalance/"+par1)
	resp = api.read()
	
	satoshi = float(resp)
	btc = satoshi/100000000
	
	return "Balance: " + str(btc)
