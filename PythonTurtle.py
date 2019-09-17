#cerner_2^5_2019
from turtle import *
color('blue')
style = ('Jacob', 30, 'bold')
write('Try Python Turtle', font=style, align='left')
hideturtle()
color('blue', 'light green')
begin_fill()
while True:
    forward(100)
    right(50)
    if abs(pos()) < 1:
        break
end_fill()
done()

