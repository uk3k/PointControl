#!/usr/bin/env python
# -*- coding: utf-8 -*-
# servoctl.py

from __future__ import division
from Tkinter import *
import ttk
import time
import tkFont

############# Basic Servo Driver ########
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685() #I2C Address
pwm.set_pwm_freq(60)

#############################################

############# main window #############
mainWin = Tk()
mainWin.title('Point Control')

mainFrame = ttk.Frame(mainWin, width=1200, height=600, borderwidth=1, relief='sunken', padding="10")
mainFrame.grid_propagate(0)
mainFrame.grid()

#############################################

############# text variables #############
tname = "Weiche Kanal "
tpos1 = "Position 1: "
tpos2 = "Position 2: "
tbset = "Aktivieren"

############# style variables #############
lstyle = tkFont.Font(family="Arial", size=17, weight="bold", underline=1)    #label style
nstyle = tkFont.Font(family="Arial", size=13, weight="bold")     #name of fields style
vstyle = tkFont.Font(family="Arial", size=14, weight="bold")     #value style
padx    = 10    #padding X
pady    = 5     #padding y
pady_b2 = 10    #padding y button 2

#############################################



############# Point Channel 0 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=0, row=0)
slabel = ttk.Label(frm, text=tname + "0", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s0p1 = IntVar()
s0p2 = IntVar()
s0p1.set(301)   #preset pos 1
s0p2.set(501)   #preset pos 2 
def p0p1():
	pwm.set_pwm(0, 0, s0p1.get())
def p0p2():
	pwm.set_pwm(0, 0, s0p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s0p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s0p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p0p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p0p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################


############# Point Channel 1 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=1, row=0)
slabel = ttk.Label(frm, text=tname + "1", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s1p1 = IntVar()
s1p2 = IntVar()
s1p1.set(311)   #preset pos 1
s1p2.set(511)   #preset pos 2 
c_label = 0     #column labels
c_entry = 1     #column entries
c_buttn = 2     #column buttons
def p1p1():
	pwm.set_pwm(1, 0, s1p1.get())
def p1p2():
	pwm.set_pwm(1, 0, s1p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s1p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s1p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p1p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p1p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################


############# Point Channel 2 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=2, row=0)
slabel = ttk.Label(frm, text=tname + "2", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s2p1 = IntVar()
s2p2 = IntVar()
s2p1.set(321)   #preset pos 1
s2p2.set(521)   #preset pos 2 
def p2p1():
	pwm.set_pwm(2, 0, s2p1.get())
def p2p2():
	pwm.set_pwm(2, 0, s2p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s2p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s2p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p2p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p2p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################


############# Point Channel 3 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=3, row=0)
slabel = ttk.Label(frm, text=tname + "3", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s3p1 = IntVar()
s3p2 = IntVar()
s3p1.set(331)   #preset pos 1
s3p2.set(531)   #preset pos 2 
def p3p1():
	pwm.set_pwm(3, 0, s3p1.get())
def p3p2():
	pwm.set_pwm(3, 0, s3p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s3p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s3p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p3p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p3p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################


############# Point Channel 4 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=0, row=1)
slabel = ttk.Label(frm, text=tname + "4", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s4p1 = IntVar()
s4p2 = IntVar()
s4p1.set(341)   #preset pos 1
s4p2.set(541)   #preset pos 2 
def p4p1():
	pwm.set_pwm(4, 0, s4p1.get())
def p4p2():
	pwm.set_pwm(4, 0, s4p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s4p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s4p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p4p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p4p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################


############# Point Channel 5 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=1, row=1)
slabel = ttk.Label(frm, text=tname + "5", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s5p1 = IntVar()
s5p2 = IntVar()
s5p1.set(351)   #preset pos 1
s5p2.set(551)   #preset pos 2 
def p5p1():
	pwm.set_pwm(5, 0, s5p1.get())
def p5p2():
	pwm.set_pwm(5, 0, s5p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s5p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s5p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p5p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p5p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################


############# Point Channel 6 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=2, row=1)
slabel = ttk.Label(frm, text=tname + "6", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s6p1 = IntVar()
s6p2 = IntVar()
s6p1.set(361)   #preset pos 1
s6p2.set(561)   #preset pos 2 
def p6p1():
	pwm.set_pwm(6, 0, s6p1.get())
def p6p2():
	pwm.set_pwm(6, 0, s6p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s6p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s6p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p6p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p6p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################


############# Point Channel 7 #############
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=3, row=1)
slabel = ttk.Label(frm, text=tname + "7", font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

############# settings
s7p1 = IntVar()
s7p2 = IntVar()
s7p1.set(371)   #preset pos 1
s7p2.set(571)   #preset pos 2 
def p7p1():
	pwm.set_pwm(7, 0, s6p1.get())
def p7p2():
	pwm.set_pwm(7, 0, s6p2.get())

entry_1 = ttk.Entry(sfrm, textvariable=s7p1, font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=s7p2, font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm,     command=p7p1, text=tbset)
buttn_2 = ttk.Button(sfrm,     command=p7p2, text=tbset)

label_1 = ttk.Label(sfrm, text=tpos1, font=nstyle, justify=RIGHT)
label_2 = ttk.Label(sfrm, text=tpos2, font=nstyle, justify=RIGHT)

entry_1.grid(column=1, row=1)
entry_2.grid(column=1, row=2)
buttn_1.grid(column=2, row=1, padx=padx, pady=pady)
buttn_2.grid(column=2, row=2, padx=padx, pady=pady_b2)
label_1.grid(column=0, row=1, padx=padx, pady=pady)
label_2.grid(column=0, row=2, padx=padx, pady=pady)

#############################################
#############################################

mainWin.mainloop()
