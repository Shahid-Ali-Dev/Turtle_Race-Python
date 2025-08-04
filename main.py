from turtle import Turtle, Screen
import random
t = Turtle()
screen = Screen()
screen.setup(600, 600)
colors = ["red", "blue", "green", "coral", "brown"]
d = Turtle()
e = Turtle()
f = Turtle()
g = Turtle()
lst = [t, d, e, f, g]

def s(i, z):
    i.penup()
    i.goto(-270,-60 + z)
    i.setheading(0)

def fo(g):
    g.forward(random.randint(1,10))

n = 0
ask = screen.textinput("Choose a colour","Which turtle do you think would win the race? ").lower()

for i in range(len(lst)):
    lst[i].color(colors[i])
    lst[i].shape("turtle")
    s(lst[i],n)
    n += 30

def win(f):
    return f.xcor()

game_over = True
while game_over:
    for i in lst:
        fo(i)
    winner = [t, d, e, f, g]
    for i in range(len(winner)):
        if int(win(winner[i])) >= 273:
            winner = winner[i]
            game_over = False
            if winner.color()[0] == ask:
                print("Congratulations, your turtle won the race")
            else:
                print("Sorry your Turtle lost the race")
            break


screen.listen()

screen.exitonclick()