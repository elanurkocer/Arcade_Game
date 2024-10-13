from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) #ilk konumun (0,0) dan başlayıp sürüklenmesini engelliyor yani direkt (350,0) konumunda başlıyor turtle'ımız

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

    
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



the_show_must_go_on = True

while the_show_must_go_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() < 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()



















screen.exitonclick()
