import turtle
import random
import time

score = 0
game_over = False

drawing_board = turtle.Screen()
drawing_board.title("Catch The Turtle")
drawing_board.bgcolor("black")

turtle_score = turtle.Turtle()
turtle_timer = turtle.Turtle()
turtle_instance = turtle.Turtle()


def timer_turtle(time):
    global game_over
    turtle_timer.hideturtle()
    turtle_timer.penup()
    turtle_timer.color("white")
    top_height = drawing_board.window_height() / 2
    y = top_height - top_height / 10
    turtle_timer.setposition(0, y - 25)
    turtle_timer.clear()

    if time > 0:
        turtle_timer.clear()
        turtle_timer.write(f"Süre: {time}", font=('Arial', 20, 'normal'))
        drawing_board.ontimer(lambda: timer_turtle(time - 1), 1000)
    else:
        game_over = True
        turtle_timer.clear()
        turtle_timer.write("Game Over!", font=('Arial', 20, 'normal'))


def score_turtle():
    turtle_score.hideturtle()
    turtle_score.penup()
    turtle_score.color("white")
    top_height = drawing_board.window_height() / 2
    y = top_height - top_height / 10
    turtle_score.setposition(0, y)
    turtle_score.write(f"Skor: {score}", font=('Arial', 20, 'normal'))


def moving_turtle():
    turtle_instance.color("white")
    turtle_instance.shape("turtle")
    turtle_instance.penup()
    turtle_instance.shapesize(3, 3)
    turtle_instance.speed(3)

    def add_score(x, y):
        global score
        score += 1
        turtle_score.clear()
        turtle_score.write(f"Skor: {score}", font=('Arial', 20, 'normal'))

    while not game_over:
        x = random.randint(-200, 200)
        y = random.randint(-300, 300)
        turtle_instance.hideturtle()
        turtle_instance.goto(x, y)
        turtle_instance.showturtle()
        time.sleep(0.5)
        turtle_instance.onclick(add_score)
        turtle_instance.hideturtle()


score_turtle()
timer_turtle(10)
moving_turtle()

turtle.mainloop()
