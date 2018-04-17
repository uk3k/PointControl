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

mainFrame = ttk.Frame(mainWin, width=1145, height=600, borderwidth=1, relief='sunken', padding="10")
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
padx    = 5    #padding X
pady    = 5     #padding y
pady_b2 = 5    #padding y button 2

############# index variables #############
pid  = IntVar()
spid = StringVar()
pos1 = [0,1,2,3,4,5,6,7]        #8 Points
pos2 = [0,1,2,3,4,5,6,7]        #8 Points

for i in range(0, 8):           #8 Points
        pos1[i] = IntVar()
        pos2[i] = IntVar()
        (i)
#############################################
#############################################

        
############# Point Channel 0 #############
############# settings
col = 0                 #column of mainFrame 
row = 0                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 0                 #point id
pos1[pid].set(301)      #preset pos 1
pos2[pid].set(501)      #preset pos 2
def set1():
        pwm.set_pwm(0, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(0, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
############# settings
col = 1                 #column of mainFrame 
row = 0                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 1                 #point id
pos1[pid].set(311)      #preset pos 1
pos2[pid].set(511)      #preset pos 2
def set1():
        pwm.set_pwm(1, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(1, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
############# settings
col = 2                 #column of mainFrame 
row = 0                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 2                 #point id
pos1[pid].set(321)      #preset pos 1
pos2[pid].set(521)      #preset pos 2
def set1():
        pwm.set_pwm(2, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(2, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
############# settings
col = 3                 #column of mainFrame 
row = 0                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 3                 #point id
pos1[pid].set(331)      #preset pos 1
pos2[pid].set(531)      #preset pos 2
def set1():
        pwm.set_pwm(3, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(3, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
############# settings
col = 0                 #column of mainFrame 
row = 1                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 4                 #point id
pos1[pid].set(341)      #preset pos 1
pos2[pid].set(541)      #preset pos 2
def set1():
        pwm.set_pwm(4, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(4, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
############# settings
col = 1                 #column of mainFrame 
row = 1                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 5                 #point id
pos1[pid].set(351)      #preset pos 1
pos2[pid].set(551)      #preset pos 2
def set1():
        pwm.set_pwm(5, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(5, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
############# settings
col = 2                 #column of mainFrame 
row = 1                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 6                 #point id
pos1[pid].set(361)      #preset pos 1
pos2[pid].set(561)      #preset pos 2
def set1():
        pwm.set_pwm(6, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(6, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
############# settings
col = 3                 #column of mainFrame 
row = 1                 #row of mainFrame
pad = 5                 #padx/pady of mainframe
pid = 7                 #point id
pos1[pid].set(371)      #preset pos 1
pos2[pid].set(571)      #preset pos 2
def set1():
        pwm.set_pwm(7, 0, pos1[pid].get())      #set first number after clamp to pwm channel
def set2():
        pwm.set_pwm(7, 0, pos2[pid].get())      #set first number after clamp to pwm channel
        
############# frame
frm = ttk.Frame(mainFrame, borderwidth=2, relief='ridge', padding="2")
frm.grid(column=col, row=row, padx=pad, pady=pad)
slabel = ttk.Label(frm, text=tname + str(pid), font=lstyle)
slabel.grid()

############# sub frame
sfrm = ttk.Frame(frm, padding="5")
sfrm.grid()

entry_1 = ttk.Entry(sfrm, textvariable=pos1[pid], font=vstyle, width=5, justify=CENTER)
entry_2 = ttk.Entry(sfrm, textvariable=pos2[pid], font=vstyle, width=5, justify=CENTER)
buttn_1 = ttk.Button(sfrm, command=set1, text=tbset)
buttn_2 = ttk.Button(sfrm, command=set2, text=tbset)
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
