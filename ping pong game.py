from turtle import *
import turtle

class paddle_A:
    paddle_a_2=None
    def __init__(self):
        self.paddle_a=turtle.Turtle()
        self.paddle_a.shape("square")
        self.paddle_a.shapesize(6,1)
        self.paddle_a.penup()
        self.paddle_a.goto(310,0)
        self.paddle_a.color("Red")
        paddle_A.paddle_a_2=self
       

    @staticmethod
    def paddle_a_up():
        y=paddle_A.paddle_a_2.paddle_a.ycor()
        y+=20
        paddle_A.paddle_a_2.paddle_a.sety(y)

    @staticmethod
    def paddle_a_down():
        y=paddle_A.paddle_a_2.paddle_a.ycor()
        y-=20
        paddle_A.paddle_a_2.paddle_a.sety(y)

class paddle_B:
    paddle_b_2=None
    def __init__(self):
        self.paddle_b=turtle.Turtle()
        self.paddle_b.shape("square")
        self.paddle_b.shapesize(6,1)
        self.paddle_b.penup()
        self.paddle_b.goto(-310,0)
        self.paddle_b.color("Blue")
        paddle_B.paddle_b_2=self

    @staticmethod
    def paddle_b_up():
        y=paddle_B.paddle_b_2.paddle_b.ycor()
        y+=20
        paddle_B.paddle_b_2.paddle_b.sety(y)

    @staticmethod
    def paddle_b_down():
        y=paddle_B.paddle_b_2.paddle_b.ycor()
        y-=20
        paddle_B.paddle_b_2.paddle_b.sety(y)

class ball:
    ball_2=None
    def __init__(self):
        self.ball=turtle.Turtle()
        self.ball.shape("circle")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.color("red")
        self.ball.shapesize(1,1)
        self.ball.dy=-2
        self.ball.dx=2
        ball.ball_2=self
        ball.ball_2.move()
    
    
    
    def move(self):
        while True:
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)
            self.wall_tap()
            self.paddle_tap()
            screen.window.win.update()

    
    def wall_tap(self):
        if self.ball.ycor()<-240:
            self.ball.dy *= -1
            
        if self.ball.ycor()>240:
            self.ball.dy *= -1

        if self.ball.xcor()>340:
            self.ball.goto(0,0)
            self.ball.dx *= -1
            screen.scr_board.clear()
            screen.player_a_score+=1
            screen.scr_board.hideturtle()
            screen.scr_board.goto(-300,200)
            screen.scr_board.color("royal blue")
            screen.scr_board.write(f"Player A:{screen.window.player_a_score}",font=("Agency",30))
            
            
            

            screen.window.win.update()    
        
        if self.ball.xcor()<-340:
            self.ball.goto(0,0)
            
            self.ball.dx *= -1
            screen.scr_board_2.clear()
            screen.player_b_score+=1
            screen.scr_board_2.hideturtle()
            screen.scr_board_2.goto(100,200)
            screen.scr_board_2.color("red")
            screen.scr_board_2.write(f"Player B:{screen.player_b_score}",font=("Agency",30))
              
            
    
    def paddle_tap(self):
        if (self.ball.xcor()>300) and (self.ball.xcor()<310) and (self.ball.ycor()<paddle_A.paddle_a_2.paddle_a.ycor()+60) and (self.ball.ycor()>paddle_A.paddle_a_2.paddle_a.ycor()-60):
            self.ball.dx *= -1

        if (self.ball.xcor()<-300) and (self.ball.xcor()>-310) and (self.ball.ycor()<paddle_B.paddle_b_2.paddle_b.ycor()+60) and (self.ball.ycor()>paddle_B.paddle_b_2.paddle_b.ycor()-60):
            self.ball.dx *= -1



    

        




class screen:
    player_a_score=0
    player_b_score=0
    window=None
    scr_board=None
    scr_board_2=None
    def __init__(self):
        turtle.bgcolor("Black")
        self.win=Screen()
        self.win.setup(width=700,height=500)
        
        screen.window=self
        self.paddle_controls()
        self.score_board()
    
    
    def call_screen(self):
        paddle_B()
        paddle_A()
        ball()
        self.win
        self.update_screen()

    @staticmethod
    def paddle_controls():
        screen.window.win.listen()
        screen.window.win.onkeypress(paddle_A.paddle_a_up, "Up")
        screen.window.win.onkeypress(paddle_A.paddle_a_down, "Down")
        screen.window.win.onkeypress(paddle_B.paddle_b_up, "w")
        screen.window.win.onkeypress(paddle_B.paddle_b_down, "s")

    
    def score_board(self):
        
        screen.scr_board=turtle.Turtle()
        screen.scr_board.hideturtle()
        screen.scr_board.goto(-300,200)
        screen.scr_board.color("royal blue")
        screen.scr_board.write(f"Player A:{self.player_a_score}",font=("Agency",30))

        screen.scr_board_2=turtle.Turtle()
        screen.scr_board_2.hideturtle()
        screen.scr_board_2.goto(100,200)
        screen.scr_board_2.color("red")
        screen.scr_board_2.write(f"Player B:{self.player_b_score}",font=("Agency",30))
        

    
    
    def update_screen(self):
        while True:
            ball.ball_2.move()
            self.win.update()

screen()
screen.window.call_screen()

