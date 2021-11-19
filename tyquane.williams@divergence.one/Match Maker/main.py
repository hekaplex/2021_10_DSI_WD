import random
import time
from tkinter import Tk, Button, DISABLED # This is an imported library


win = Tk()
win.title('Matchmaker')
win.resizable(width=False, height=False)
false = True
previousx = 0
previousy = 0

buttons = {}
button_symbols = {}

symbols=[u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
         u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
         u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
         u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbols)


for x in range(6):
    for y in range(4):
        button = Button(width=10, height=8)
        button.grid(column=x, row=y)
        buttons[x,y]=button
        button_symbols[x,y]=symbols.pop()




win.mainloop()
