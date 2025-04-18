import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter
from math import sqrt
""" Plot of secant method

    f(x)
        evaluate the function of the bisection method and plot it
    df read the csv file

    init()
        function for the animation, init all the values to be changing
    update(i)
        make the update when found the i row
        getting a,b,c,fa,fb,fc,error and displaying on the animation
"""
    

def f(x):
    return x**3+(4*x*x)-10

df = pd.read_csv("../data/secant_output.csv")

x_vals = np.linspace(-1,3,300)
y_vals = f(x_vals)

# Plot the function on a range
fig , ax = plt.subplots()
ax.plot(x_vals,y_vals, label = "f(x)" , color = "teal")
ax.axhline(0,color="black",linewidth = 0.8)
ax.legend()

#Some global variables for the init and update
point1, = ax.plot([],[],'ro')
point2, = ax.plot([],[],'ro')
point3, = ax.plot([],[],'ro')
line1, = ax.plot([],[],'b--')
line2, = ax.plot([],[],'r--')
text_box = ax.text(0.05,0.95,'')

def init():
    point1.set_data([],[])
    point2.set_data([],[])
    point3.set_data([],[])
    line1.set_data([],[])
    line2.set_data([],[])
    text_box = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=10,verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    return point1,point2,point3,line1,line2

def update(i):
    row = df.iloc[i]
    a,b,c,fa,fb,fc,error = row['xa'],row['xb'],row['xc'],row['ya'],row['yb'],row['yc'],row['error']
    text = (
        f"Iter: {i+1}\n"
        f"xa = {a:.6f}\n"
        f"xb = {b:.6f}\n"
        f"xc = {c:.6f}\n"
        f"ya = {fa:.2e}\n"
        f"yb = {fb:.2e}\n"
        f"yc = {fc:.2e}\n"
        f"error = {error:.2e}"
    )
    text_box.set_text(text)
    point1.set_data([a],[fa])
    point2.set_data([b],[fb])
    point3.set_data([c],[0])
    line1.set_data([a,b],[fa,fb])
    line2.set_data([c,0],[c,-10000000])
    return point1,point2,point3,line1,line2,text_box

# Making the animation with 0.8 seconds btw iterations
animation = FuncAnimation(fig,update,frames = len(df),init_func=init,blit=True,interval = 800,repeat = False)

animation.save("../animations/secant.gif",writer=PillowWriter(fps=1))

#Showing the animation, debug
plt.show()

