import tkinter as tk
import eventHandlers as EH

window = tk.Tk() # creates instance of tkinter class

frame1 = tk.Frame(master=window, width=100, height=100, bg='blue') # frame for the whole application

# Minus 1 Button
minus_btn = tk.Button(master=frame1, text='-', bg='red')
minus_btn.pack(side=tk.LEFT)

# Result display
display_lbl = tk.Label(master=frame1, text='0', bg='yellow')
display_lbl.pack(side=tk.LEFT)

# Add 1 Button
add_btn = tk.Button(master=frame1, text='+', bg='green', command=EH.increase_res)
add_btn.pack(side=tk.LEFT)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # frame set to expand and be responsive no matter window size

window.mainloop() # executes the tkinter event loop