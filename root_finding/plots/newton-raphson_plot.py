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
    return 230*(x**4) + 18*(x**3)+9*x*x - 221*x-9

df = pd.read_csv("../data/newton-raphson_output.csv")

x_vals = np.linspace(-3,3,500)
y_vals = f(x_vals)

# Plot the function on a range
fig , ax = plt.subplots()
ax.plot(x_vals,y_vals, label = "f(x)" , color = "teal")
ax.axhline(0,color="black",linewidth = 0.8)
ax.legend()

#Some global variables for the init and update
point1, = ax.plot([],[],'ro')
point2, = ax.plot([],[],'ro')
line, = ax.plot([],[],'b--')
text_box = ax.text(0.05,0.95,'')

def init():
    point1.set_data([],[])
    point2.set_data([],[])
    line.set_data([],[])
    text_box = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=10,verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    return point1,point2,line

def update(i):
    row = df.iloc[i]
    a,b,error = row['xn'],row['xn1'],row['error']
    text = (
        f"Iter: {i+1}\n"
        f"x_i = {a:.6f}\n"
        f"x_i+1 = {b:.6f}\n"
        f"error = {error:.2e}"
    )
    text_box.set_text(text)
    point1.set_data([a],[f(a)])
    point2.set_data([b],[0])
    line.set_data([a,b],[f(a),0])
    return point1,point2,line,text_box

# Making the animation with 0.8 seconds btw iterations
animation = FuncAnimation(fig,update,frames = len(df),init_func=init,blit=True,interval = 800,repeat = False)

animation.save("../animations/newton-raphson.gif",writer=PillowWriter(fps=1))

#Showing the animation, debug
plt.show()

