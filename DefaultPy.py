#!/usr/bin/python

#Imports

#Consts
TITLE="Software"

#Variables


#Functions

#fncInitVariables
#def fncInitVariables():

#fncWelcomeScreen
def fncWelcomeScreen():
	print "=============================="
	print "Welcome to" + TITLE
	print "=============================="
        #fncInitVariables()

#fncExit
def fncExit():
    raw_input("Press any key to Exit")

def fncMain():
	fncInitVariables()
        fncWelcomeScreen()


#Main Program
fncMain()
fncExit()
