# What is  Varas

#### Varas is a simple skype bot with a plugin system written in Python.

<p align="center"><img src="http://i.imgur.com/IJJf7XE.jpg" /></p><br>

# Running Varas on Linux

### Requirements 

* Python installed on your computer (Under Python3)
* Brain

#### Once moved to the directory where you cloned the repo with the terminal just type:

* python Bot.py

## Creating a Plugin

* First step move to the /Plugins directory.
* Create a new file whose extension will be .py
* Open it and define a description:
```python
desc = "The description of the plugin."
```
* Once you're done with the description create the execution function:
```python
def execute():
  return "Hello World."
  #This will make the bot send 'Hello World.' on the chat you've typed the command.
```
* You can also pass up to 4 parameters to the function:
```python
def execute(one,two,three,four):
  return one+two+three+four
  #This will make the bot send 'the sum of the 4 parameters in the chat you've typed the command
```

* For further examples look at the help.py plugin and exampleplugin.py [here](https://github.com/GooogIe/Varas/tree/master/Plugins)

***
# More #

### Contributors:

* Neon/Loled

### You can find me on:

* [Holeboards](http://www.holeboards.eu/User-u0qq%C9%90H)
* [Telegram](http://www.telegram.me/DonaldTrvmp)
* Skype: pybot.py

