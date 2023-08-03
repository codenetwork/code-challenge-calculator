from turtle import *
speed("fast")

# draw the x and y axes
pu()
goto(-250, 0)
pd()
goto(250, 0)
pu()
goto(0, 250)
pd()
goto(0,-250)

# draw the notches
for x in range(-240, 240, 20):
    pu()
    goto(x, 5)
    write(x//20)
    pd()
    goto(x, -5)

for y in range(-240, 240, 20):
    pu()
    goto(-5, y)
    pd()
    goto(5, y)
    write(y//20)

# enter some values
startx = int(input("Enter your start x value: "))
endx = int(input("Enter your end x value: "))
equation = input("Enter your equation (x is the variable): ")

# begin graphing
pu()
goto(startx*20, eval(equation, {"x": startx})*20)
pd()
for x in range(startx, endx):
    print(x, eval(equation))
    goto(x*20, eval(equation)*20)

# label the graph
pu()
goto(200, 200)
write(equation)

done()