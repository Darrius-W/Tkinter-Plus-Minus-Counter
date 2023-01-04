import tkinter as tk

# EVENT HANDLERS
#----------------------------------------------------------------------
def increase_res():
    result = display_lbl['text']
    result = int(display_lbl['text']) + 1
    display_lbl['text'] = result
    
def decrease_res():
    if int(display_lbl['text']) <= 0: # if result becomes less than 0
        pass
    else: # if result is greater than 0
        result = display_lbl['text']
        result = int(display_lbl['text']) - 1
        display_lbl['text'] = result
#----------------------------------------------------------------------
    
    
    
# MAIN
#----------------------------------------------------------------------
window = tk.Tk() # creates instance of tkinter class
window.resizable(0,0)
window.title('Plus-Minus Counter')

frame1 = tk.Frame(master=window, bg='black') # frame for the whole application

# Minus 1 Button
minus_btn = tk.Button(master=frame1, text='-', bg='red', width=12, height=5, command=decrease_res, relief=tk.RAISED)
minus_btn.pack(fill=tk.Y, side=tk.LEFT)

# Result display
display_lbl = tk.Label(master=frame1, text='0', width=12, height=5, bg='yellow', relief=tk.FLAT)
display_lbl.pack(fill=tk.Y, side=tk.LEFT)

# Add 1 Button
add_btn = tk.Button(master=frame1, text='+', bg='green', width=12, height=5, command=increase_res, relief=tk.RAISED)
add_btn.pack(fill=tk.Y, side=tk.LEFT)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # frame set to expand and be responsive no matter window size

window.mainloop() # executes the tkinter event loop
#----------------------------------------------------------------------