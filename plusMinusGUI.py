import tkinter as tk

# EVENT HANDLERS
def increase_res():
    result = display_lbl['text']
    result = int(display_lbl['text']) + 1
    display_lbl['text'] = result
    
def decrease_res():
    if int(display_lbl['text']) <= 0:
        pass
    else:
        result = display_lbl['text']
        result = int(display_lbl['text']) - 1
        display_lbl['text'] = result
    
    

window = tk.Tk() # creates instance of tkinter class

frame1 = tk.Frame(master=window, width=100, height=100, bg='blue') # frame for the whole application

# Minus 1 Button
minus_btn = tk.Button(master=frame1, text='-', bg='red', command=decrease_res)
minus_btn.pack(side=tk.LEFT)

# Result display
display_lbl = tk.Label(master=frame1, text='0', bg='yellow')
display_lbl.pack(side=tk.LEFT)

# Add 1 Button
add_btn = tk.Button(master=frame1, text='+', bg='green', command=increase_res)
add_btn.pack(side=tk.LEFT)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # frame set to expand and be responsive no matter window size

window.mainloop() # executes the tkinter event loop