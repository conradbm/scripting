x= arange(-3,10.1,0.1)
y= arange(-3,10.1,0.1)
y1= 0.4*x-2.0
y2= 4.0-0.5*x

xlim(-3,10)
ylim(-3,10)
hlines(0,-3,10,color='k')
vlines(0,-3,10,color='k')
grid(True)

xlabel('x-axis')
ylabel('y-axis')
title ('Shaded Area Shows the Feasible Region')

plot(x,y1,color='b')
plot(x,y2,color='r')
legend(['2x-5y=10','x+2y=8'])

x= [0.0, 0.0, 6.67,5.0]
y= [0.0, 4.0, .67, 0.0]
fill(x,y)
show()
