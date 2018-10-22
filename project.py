
import matplotlib.pyplot as plot
def f(x, y):
    return x**3*y**4-y/x
def f_improved(x,y,h):
    return y+h/2*(f(x,y)+f(x+h, y+h*f(x,y)))
def f_euler(x, y, h):
    return y+h*f(x,y)
  
n=10
x0=1
y0=0.5
x=5
h=(x-x0)/n
x_v=[x0]
y_euler=[y0]
y_original=[y0]
y_improved=[y0]
e=[0]

i=x0
while (i<x):
    y_original.append((11-3*x_v[-1])**(-1/3))
    y_euler.append(f_euler(y_v[-1],x_v[-1], h))
    y_improved.append(f_improved(x_v[-1], y_improved[-1], h))
    x_v.append(i)
    e.append(y_v[-1]-y_original[-1])
    i+=h
    print(i)
    
plot.plot(x_v, y_euler)
plot.show()

plot.plot(x_v, y_original)
plot.show()

plot.plot(x_v, e)
plot.show()

plot.plot(x_v, y_improved)
plot.show()

