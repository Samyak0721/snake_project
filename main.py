import turtle
import time
import random

delay = 0.1

# scores
score = 0
high_score = 0

# set up screen
t = turtle.Screen()
t.title("Snacky")
t.bgcolor('pink')
t.tracer(0) #automatic screen are updates are off.

#head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("blue")
food.penup()

segments = []

# scorecards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("red")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("Score: 0  High score: 0", align="center", font=("calibri", 32, "bold"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()  #will return y coordinate of current position of turtle
        head.sety(y + 20)  #increase y coordinate if head goes up
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
t.listen()
t.onkeypress(go_up, "8")
t.onkeypress(go_down, "2")
t.onkeypress(go_left, "4")
t.onkeypress(go_right, "6")

# MainLoop
while True:
    t.update()

    # check collision with the border
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1) #ends execution
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments of body as the snake has died
        for segment in segments:
            segment.goto(1000, 1000)  # out of range
        # clear the segments
        segments.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.1

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("calibri", 32, "normal"))

    # check collision with food
    if head.distance(food) < 25:
        # move the food to random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001
        # increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()  #to del turtle's drawing from screen
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("calibri", 32, "normal"))

    # move the segments in reverse order for rest segments except the head one
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1

            # update the score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                     font=("calibri", 32, "normal"))
    time.sleep(delay)
wn.mainloop()
