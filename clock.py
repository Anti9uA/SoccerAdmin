import time as tm
from tkinter import *

def display_time():
    current_time = tm.strftime(' %m월 %d일 (%a) %I:%M ')
    clock_label['text'] = current_time
    win.after(1000, display_time)
win = Tk()
win.title('Current Time')
clock_label=Label(win, font='ariel 90', fg = 'black')
clock_label.grid(row=0, column=0)
display_time()
win.mainloop()