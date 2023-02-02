import random
import time

tela = turtle.Screen()
tela.title("SNAKE GAME DESU")

score = 0
time = 60
snake_size = 0

tela.bgcolor('black')
tela.setup(width=600, height=600)
tela.tracer(0)

#here comes the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('white')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#here comes the food
food = turtle.Turtle()
food.speed(0)
food.shape('triangle')
food.color('yellow')
food.penup()
food.goto(100,100)

def go_right():
    snake.direction = 'right'

def go_left():
    snake.direction = 'left'

def go_up():
    snake.direction = 'up'

def go_down():
    snake.direction = 'down'

def go_center():
    snake.goto(0,0)

tela.listen()
tela.onkeypress(go_right, "Right")
tela.onkeypress(go_left, "Left")
tela.onkeypress(go_up, "Up")
tela.onkeypress(go_down, "Down")

## game starts here

while time > 0:
    tela.update()
    if snake.distance(food) < 10:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        snake_size = snake_size +1
        score = score +10
        tela.title(f'Score: {score}')

    time.sleep(0.1)
    time = time - 0.1
    tela.title(f'Time{time} - Score:{score}')

    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 10)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 10)
    if snake.direction == 'up':
        x = snake.ycor()
        snake.setx(y + 10)
    if snake.direction == 'down':
        x = snake.ycor()
        snake.setx(y - 10)

## game ends here

tela.title(f'GAME OVER! Final score:{score}')
snake.goto(0,0)
snake.direction = 'stop'
tela.mainloop()