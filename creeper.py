from turtle import *
sc=Screen()
sc.setup(width=1.0,height=1.0)
speed(10)
colormode(255)
pixel=20

penup()
goto(-80,80)
pendown()

pencolor(56, 177, 72)
fillcolor(56, 177, 72)
def s(size):
    for a in range(4):
        forward(size)
        right(90)


begin_fill()
s(pixel*8)
end_fill()

pencolor('black')
penup()
goto(-60,40)
pendown()

fillcolor('black')
begin_fill()
s(pixel*2)
end_fill()

penup()
goto(20,40)
pendown()
begin_fill()
s(pixel*2)
end_fill()

r=right
l=left

def m():
    penup()
    goto(0,0)
    pendown()
    forward(pixel)
    r(90)
    forward(pixel)
    l(90)
    forward(pixel)
    r(90)
    forward(pixel*3)
    r(90)
    forward(pixel)
    r(90)
    forward(pixel)
    l(90)
    forward(pixel)

begin_fill()
m()
l=right
r=left
m()
goto(0,0)
left(90)
end_fill()


done()