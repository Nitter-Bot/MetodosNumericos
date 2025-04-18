import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,PillowWriter

""" Plot of the bisection method

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
    return x-2**(-x)

df = pd.read_csv("../data/bisection_output.csv")

x_vals = np.linspace(-1,3,500)
y_vals = f(x_vals)

# Plot the function on a range
fig , ax = plt.subplots()
ax.plot(x_vals,y_vals, label = "f(x)" , color = "teal")
ax.axhline(0,color="black",linewidth = 0.8)
ax.legend()

#Some global variables for the init and update
point, = ax.plot([],[],'ro')
line, = ax.plot([],[],'r--')
text_box = ax.text(0.05,0.95,'')

def init():
    point.set_data([],[])
    line.set_data([],[])
    text_box = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=10,verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    return point,line

def update(i):
    row = df.iloc[i]
    a,b,c,fa,fb,fc,error = row['a'],row['b'],row['c'],row['fa'],row['fb'],row['fc'],row['error']
    text = (
        f"Iter: {i+1}\n"
        f"a = {a:.6f}\n"
        f"b = {b:.6f}\n"
        f"c = {c:.6f}\n"
        f"f(a) = {fa:.2e}\n"
        f"f(b) = {fb:.2e}\n"
        f"f(c) = {fc:.2e}\n"
        f"error = {error:.2e}"
    )
    text_box.set_text(text)
    point.set_data([c],[fc])
    line.set_data([a,b],[fa,fb])
    return point,line,text_box

# Making the animation with 0.8 seconds btw iterations
animation = FuncAnimation(fig,update,frames = len(df),init_func=init,blit=True,interval = 800,repeat = False)

animation.save("../animations/bisection.gif",writer=PillowWriter(fps=1))

#Showing the animation, debug
plt.show()

