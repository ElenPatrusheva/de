import matplotlib.pyplot as plot

def f(x, y):
    return x**3*y**4-y/x
    
def f_euler(x, y, h):
    return y+h*f(x,y)

def f_improved(x, y, h):
    return y+h/2*(f(x,y)+f(x+h, y+h*f(x,y)))

def f_runge(x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h/2 * k1)
    k3 = f(x + h/2, y + h/2 * k2)
    k4 = f(x + h, y + h * k3)
    return y + h/6 * (k1 + 2*k2 +2*k3 + k4)

main(){
	x=[x0]
	y_euler=[y0]
	y_original=[y0]
	y_improved=[y0]
	y_runge=[y0]
	e=[0]
	i=x0

	while (i<xf):
    	y_original.append(x[-1]**(-1)*(11-3*x[-1])**(-1/3))
    	y_euler.append(f_euler(x[-1], y_euler[-1], h))
    	y_improved.append(f_improved(x[-1], y_improved[-1], h))
    	y_runge.append(f_runge(x[-1], y_runge[-1], h))
    	x.append(i)
    	#e.append(y_euler[-1]-y_improved[-1])
    	i+=h
    	print(i)

    plot.plot(x, y_original)
	plot.show()

	plot.plot(x, y_euler)
	plot.show()

	plot.plot(x, y_improved)
	plot.show()

	plot.plot(x, y_runge)
	plot.show()
}