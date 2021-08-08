import math
import keyboard
from threading import Thread
from tkinter import *
import time
import tkinter as tk
from tkinter.font import Font

import win32api, win32con
def click():
    while True:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,10,120,0,0)
        if keyboard.is_pressed('b'):
            print("Done")
            break
        
DELAY = 10
CIRCULAR_PATH_INCR = 0.3

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))

class Celestial(object):
    # Constants
    COS_0, COS_180 = cos(0), cos(180)
    SIN_90, SIN_270 = sin(90), sin(270)

    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def bounds(self):
        """ Return coords of rectangle surrounding circlular object. """
        return (self.x + self.radius*self.COS_0,   self.y + self.radius*self.SIN_270,
                self.x + self.radius*self.COS_180, self.y + self.radius*self.SIN_90)

def circular_path(x, y, radius, delta_ang, start_ang=0):
    """ Endlessly generate coords of a circular path every delta angle degrees. """
    ang = start_ang % 360
    while True:
        yield x + radius*cos(ang), y + radius*sin(ang)
        ang = (ang+delta_ang) % 360

def update_position(canvas, id, celestial_obj, path_iter):
    celestial_obj.x, celestial_obj.y = next(path_iter)  # iterate path and set new position
    # update the position of the corresponding canvas obj
    x0, y0, x1, y1 = canvas.coords(id)  # coordinates of canvas oval object
    oldx, oldy = (x0+x1) // 2, (y0+y1) // 2  # current center point
    dx, dy = celestial_obj.x - oldx, celestial_obj.y - oldy  # amount of movement
    canvas.move(id, dx, dy)  # move canvas oval object that much
    # repeat after delay
    canvas.after(DELAY, update_position, canvas, id, celestial_obj, path_iter)

top = tk.Tk()
top.title('UPDATE BIOS')
top.configure(bg='#08acf4')
top.config(cursor="none")

font_1 = Font(family='Arial', size=40,
 weight='bold',
              slant='italic',
              underline=0,
              overstrike=0)
font_2 = Font(family='Arial',size=30 ,weight='bold',
              slant='italic',
              underline=0,
              overstrike=0)
top.attributes('-fullscreen', True)  

canvas = tk.Canvas(top, bg='#08acf4', height=500, width=500,highlightthickness=0)
canvas.pack()
text = Label(top,text='UPDATING BIOS.DRIVERS This will take 3 hours',font=font_1,bg='#08acf4',fg='white')
text.place(x=375,y=550)
label = Label(top,text='Please do not Turn off computer that will damage your computer',font=font_2,bg='#08acf4',fg='white')
label.place(x=400,y=700)
sol_obj = Celestial(250, 250, 25)
planet_obj1 = Celestial(250+100, 250, 15)
planet1 = canvas.create_oval(planet_obj1.bounds(), fill='white', width=0)

orbital_radius = math.hypot(sol_obj.x - planet_obj1.x, sol_obj.y - planet_obj1.y)
path_iter = circular_path(sol_obj.x, sol_obj.y, orbital_radius, CIRCULAR_PATH_INCR)
next(path_iter)  # prime generator

top.after(DELAY, update_position, canvas, planet1, planet_obj1, path_iter)
x = Thread(target=click)
x.start()
top.mainloop().start()

