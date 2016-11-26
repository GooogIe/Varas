#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Host2ip plugin for Varas
Author: Neon
Last modified: November 2016
"""
import socket

desc = "Attempt to resolve an hostname."

def execute(par1):
	return str(par1+ " IP: "+socket.gethostbyname(par1))
