#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python skype bot, with a plugin system.
Read exampleplugin.py on more infos on how to create one.

Author: Habb0n and Neon

Last modified: November 2016

Version: 1.4

Github: https://github.com/GooogIe and 
"""

#Imports
import Skype4Py
import Utils
import os
import updater
from os import listdir
from os.path import isfile, join
import sys

#Don't write bytecodes file (.pyc)
sys.dont_write_bytecode = True

#Skype instance
skype = Skype4Py.Skype()

#Version
ver = 1.4

#Bot class
class Bot:
    #Constructor method
    def __init__(self, name,version,trigger,debug):
        self.name = name
        self.version = version
        self.trigger = trigger
        self.plugins = []
	self.os = os.name
	self.debug = debug
	self.config = { "Name":self.name,"Version":self.version,"Debug":self.debug,"Trigger":self.trigger}
	Utils.savefile("Config.json",self.config)
	if os == 'nt':
		self.plugindir = os.getcwd()+"\Plugins"
	else:
		self.plugindir = os.getcwd()+"/Plugins"
    #Defining basic methods

    def addplugin(self,plugin):
        self.plugins.append(plugin)

    def setname(self,name):
	self.config["Name"] = name
	self.name = name
	Utils.savefile("Config.json",self.config)

    def settrigger(self,trigger):
	self.config["Trigger"] = trigger
	self.trigger = trigger
	Utils.savefile("Config.json",self.config)

    def setversion(self,version):
	self.config["Version"] = version
	self.version = version
	Utils.savefile("Config.txt",self.config)

    def setdebug(self,debug):
	self.config["Debug"] = debug
	self.debug = debug
	Utils.savefile("Config.txt",self.config)

    def getname(self):
	return self.name

    def gettrigger(self):
	return self.trigger

    def getversion(self):
	return self.version

    def getdebug(self):
	return self.debug

    def getplugins(self):
	return Utils.Cafe+",".join(self.plugins)

    #Load the plugins to a list
    def loadplugins(self):
	for f in listdir(self.plugindir):
		if isfile(join(self.plugindir, f)):
			if(f!="__init__.py" and ".pyc" not in f):
				f =f.replace(".py",'',1)
				fl = [line.strip() for line in open(self.plugindir+"/"+f+".py", 'r')]
				if any("def execute" and "desc =" in s for s in fl):
					self.addplugin(f)
					Utils.action("Added "+Utils.Cafe+f+Utils.defcol+" plugin.")
				else:
					Utils.alert("Couldn't add "+Utils.Cafe+f+Utils.defcol+" plugin, necessary functions missing(execution and desc).")

    #Import and execute the plugin
    def callplugin(self,plugin):
	exec("from Plugins import "+plugin[0])
	if len(plugin) ==1:
		exec("tosend = "+plugin[0]+".execute()")
	elif len(plugin) == 2:
		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"')")
	elif len(plugin) == 3:
		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"','"+plugin[2]+"')")
	elif len(plugin) == 4:
		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"','"+plugin[2]+"','"+plugin[3]+"')")
	elif len(plugin) == 5:
		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"','"+plugin[2]+"','"+plugin[3]+"','"+plugin[3]+"')")
	return "[#] "+str(tosend)

    #Process the message received
    def process(self,msg,status):
	chat = msg.Chat
        send = msg.Chat.SendMessage
        senderDisplay = msg.FromDisplayName
        senderHandle = msg.FromHandle
        msg = msg.Body
	if (status == "SENT" or status == "RECEIVED") and msg.startswith(self.trigger):
		cmd = msg.replace(self.trigger,"")
		cmd = cmd.split(" ")
		if cmd[0] in self.plugins:
			Utils.action("User "+senderHandle+" performed "+cmd[0])
			if self.debug == "False":
				try:
					send(self.callplugin(cmd))
				except:
					Utils.alert("Error while performing "+cmd[0]+" ("+senderHandle+")")
					send("[#] Error while performing "+cmd[0]+" ("+senderHandle+")")
			else:
				send(self.callplugin(cmd))
		else:
			send("[#] No plugin found for "+cmd[0]+", use "+self.trigger+"help, to get a list of available commands.")
			Utils.alert("No plugin found("+cmd[0]+")")

def main():
	#Initializing bot instance
	if isfile("Config.json"):
		configs = Utils.loadfile("Config.json")
		trigger = configs["Trigger"]
		name = configs["Name"]
		version = configs["Version"]
		debug = configs["Debug"]
		myBot = Bot(name,version,trigger,debug)
	else:
		myBot = Bot("Bot","0.1","!","False")

	#Startup prints
	os.system("title Varas Bot - 1.3")
	Utils.info()
	Utils.logaction("Attaching to skype.")
	try:
		if skype.Client.IsRunning == False:
			try:
				Utils.logaction("Skype instance not found, trying to start one.")
    				skype.Client.Start()
			except:
				Utils.errorquit("Couldn't start skype, quitting...")
		skype.Attach()
		Utils.action("Attached successfully.")
	except:
		Utils.errorquit("Couldn't attach to skype, quitting...")
	Utils.logaction("Loading "+Utils.Cafe+"plugins"+Utils.defcol)
	try:
		myBot.loadplugins()
		Utils.action("Successfully loaded "+Utils.Cafe + str(len(myBot.plugins))+Utils.defcol +" plugins.")
	except:
		Utils.alert("Couldn't load plugins.")
	Utils.logaction("Checking for updates...")
	try:
		if updater.check(ver)== True:
			Utils.action("Varas is up to date!")
		else:
			Utils.alert("Update found! Type 'update' in console to update the bot.")
	except:
		Utils.alert("Couldn't check for updates.")
	#Bot infos
	Utils.logaction("Current trigger is " + Utils.Cafe+myBot.gettrigger()+Utils.defcol)
	Utils.logaction("Current bot name is " + Utils.Cafe+myBot.getname()+Utils.defcol)
	Utils.logaction("Current bot version is " + Utils.Cafe+myBot.getversion()+Utils.defcol)
	Utils.logaction("Type '"+Utils.Cafe+"help"+Utils.defcol+"' in console to view a list of console commands.")
	skype.OnMessageStatus = myBot.process

	#Loop to keep the bot active
	while True:
		cmd = raw_input(Utils.red+'>'+Utils.defcol)
		if cmd.startswith("settrigger "):
			trg = cmd.split(" ")
			myBot.settrigger(trg[1])
			Utils.action("Changed trigger to "+Utils.Cafe+trg[1]+Utils.defcol)
		if cmd.startswith("setversion "):
			vrs = cmd.split(" ")
			myBot.setversion(vrs[1])
			Utils.action("Changed version to "+Utils.Cafe+vrs[1]+Utils.defcol)
		if cmd.startswith("setname "):
			nm = cmd.split(" ")
			myBot.setname(nm[1])
			Utils.action("Changed name to "+Utils.Cafe+nm[1]+Utils.defcol)
		if cmd.startswith("setdebug "):
			db = cmd.split(" ")
			if db[1] == "True" or db[1] == "False":
				myBot.setdebug(db[1])
				Utils.action("Changed Debug mode to "+Utils.Cafe+db[1]+Utils.defcol)
			else:
				Utils.alert("Debug mode must be True or False")
		if cmd=="gettrigger":
			Utils.action("Current trigger is: "+Utils.Cafe+myBot.gettrigger()+Utils.defcol)
		if cmd=="getname":
			Utils.action("Current name is: "+Utils.Cafe+myBot.getname()+Utils.defcol)
		if cmd=="getplugins":
			Utils.action("Loaded plugins are: "+Utils.Cafe+myBot.getplugins()+Utils.defcol)
		if cmd=="getversion":
			Utils.action("Current version is: "+Utils.Cafe+myBot.getversion()+Utils.defcol)
		if cmd=="getdebug":
			Utils.action("Current debug mode is: "+Utils.Cafe+myBot.getdebug()+Utils.defcol)
		if cmd=="reload":
			Utils.action("Reloading "+Utils.Cafe+"plugins."+Utils.defcol)
			myBot.plugins = []
			myBot.loadplugins()
			Utils.action("Done reloading.")
		if cmd=="update":
			Utils.action("Attempting to update, bot will close after update.")
			Utils.action("Bot will close after being updated.")
			if updater.check(ver)==True:
				Utils.action("Varas is up to date!")
			else:
				updater.update()
		if cmd=="help":
			Utils.action("Available console commands are: "+Utils.Cafe+"help,reload,setversion <version>,getversion,setname <name>,getname,settrigger <trigger>,gettrigger,setdebug <True/False>,getdebug,update,getplugins"+Utils.defcol)

if __name__ == "__main__":
	main()
