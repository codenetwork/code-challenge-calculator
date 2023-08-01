from turtle import *

# draw the x and y axes
pu()
goto(-250, 0)
pd()
goto(250, 0)
pu()
goto(0, 250)
pd()
goto(0,-250)

startx = int(input("Enter your start x value: "))
endx = int(input("Enter your end x value: "))
equation = input("Enter your equation (x is the variable): ")

pu()
goto(startx*20, eval(equation, {"x": startx})*20)
pd()
for x in range(startx, endx):
    print(x, eval(equation))
    goto(x*20, eval(equation)*20)

done()