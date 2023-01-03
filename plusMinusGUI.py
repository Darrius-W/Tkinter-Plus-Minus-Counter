import tkinter as tk

window = tk.Tk() # creates instance of tkinter class

frame1 = tk.Frame(master=window, width=100, height=100, bg='blue') # frame for the whole application

minus_btn = tk.Button(master=frame1, text='-', bg='red')
minus_btn.pack(side=tk.LEFT)

display_lbl = tk.Label(master=frame1, text='"display num"', bg='green')
display_lbl.pack(side=tk.LEFT)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) # frame set to expand and be responsive no matter window size

window.mainloop() # executes the tkinter event loop