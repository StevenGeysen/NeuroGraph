#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""     NeuroGraph: Plotting -- Version 1
Last edit:  2024/03/15
Author:     Geysen, Steven (SG)
Notes:      - Plot NeuroGraph
            - Release notes:
                * Initial commit
To do:      - Modify pyvis
            - Plot function
Comments:   
Sources:    Python 3 Object-Oriented Programming (Phillips, 2018)
            https://python-course.eu/applications-python/graphs-python.php
            https://github.com/WestHealth/pyvis
            https://youtu.be/lVTC8CvScQo?si=j0TLG7veHihQwsRD
"""



#%% ~~ Imports ~~ %%#


import tkinter as tk
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from src.regions import Insula as Ins
from src.regions import PrefrontalCortex as pfc



#%% ~~ Variables ~~ %%#


# Initialise
## Plot
fig, ax = plt.subplots()
## tkinter
root = tk.Tk()
frame = tk.Frame(root)



#%% ~~ Plot ~~ %%#
##################


lable = tk.Label(text='NeuroGraph')
lable.config(font=('Papyrus', 32))
lable.pack()

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

frame.pack()


root.mainloop()



# ------------------------------------------------------------------------- End
