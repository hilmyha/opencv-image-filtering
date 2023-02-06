from tkinter import *
from tkinter import ttk
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def lowpass():
  os.system('python UTS/lowpass.py')

def highpass():
  os.system('python UTS/highpass.py')
  
def highboost():
  os.system('python UTS/highboost.py')

def emboss():
  os.system('python UTS/emboss.py')

def gaussian():
  os.system('python UTS/gaussian.py')

def inverse():
  os.system('python UTS/inverse.py')

def cam():
  os.system('python UTS/cam.py')

root = Tk()
frm = ttk.Frame(root, padding=40)
root.title("StreamFilt")
root.maxsize(800, 400)
frm.grid()
ttk.Label(frm, text="StreamFilt\n").grid(columnspan=2, row=1)

ttk.Button(frm, text="LOWPASS", command=lowpass).grid(column=0, row=2, sticky='ew')
ttk.Button(frm, text="HIGHPASS", command=highpass).grid(column=1, row=2, sticky='ew')
ttk.Button(frm, text="HIGHBOOST", command=highboost).grid(column=0, row=4, sticky='ew')
ttk.Button(frm, text="GAUSSIAN", command=gaussian).grid(column=1, row=4, sticky='ew')
ttk.Button(frm, text="EMBOSS", command=emboss).grid(column=0, row=6, sticky='ew')
ttk.Button(frm, text="INVERSE", command=inverse).grid(column=1, row=6, sticky='ew')

ttk.Label(frm, text="").grid(columnspan=3, row=9, sticky='ew')
ttk.Label(frm, text="Press 'space' to capture image").grid(columnspan=3, row=10, sticky='ew')
ttk.Label(frm, text="Press 'esc' to quit from cam").grid(columnspan=3, row=11, sticky='ew')
ttk.Label(frm, text="").grid(columnspan=3, row=12, sticky='ew')
ttk.Button(frm, text="CAM", command=cam).grid(columnspan=3, row=13, sticky='ew')
ttk.Button(frm, text="QUIT", command=root.destroy).grid(columnspan=3, row=14, sticky='ew')
root.mainloop()