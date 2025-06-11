import turtle
import random
import time
class Screen:
    obj=None
    
    
    def __init__(self):
        self.window=turtle.Screen()
        self.window.bgcolor("Black")
        self.window.setup(width=670,height=850)
        self.window.tracer(0)
        Screen.obj=self
        
        #scoreboard
        self.penn=turtle.Turtle()
        self.penn.hideturtle()
        self.penn.speed(100)
        self.penn.goto(-220,340)
        self.penn.color("Lime")
        self.penn.write(f"Score:",font=("Small Fonts",37))
        

        self.penn_2=turtle.Turtle()
        self.penn_2.hideturtle()
        self.penn_2.speed(100)
        self.penn_2.goto(100,340)
        self.penn_2.color("Cyan")
        self.penn_2.clear()
        self.penn_2.write(f"Score:",font=("Small Fonts",37))
        
        self.borderline()
        self.call_all_classes()
        
        turtle.done()
    
    
    def update_score(self):
        self.penn.clear()
        self.penn.write(f"Score:{Snake.snk_score}",font=("Small Fonts",37))

        self.penn_2.clear()
        self.penn_2.write(f"Score:{Snake.snk2_score}",font=("Small Fonts",37))

    
    def borderline(self):
        border_turtle=turtle.Turtle()
        border_turtle.hideturtle()
        border_turtle.speed(100)
        border_turtle.goto(-300, 300)
        border_turtle.color("red")
        border_turtle.pensize(9)
        
    
        
        for i in range(4):
            border_turtle.forward(600)
            border_turtle.right(90)
        
                                                                                                                       

    
    def call_all_classes(self):
        Snake()
        Fruit()
        self.window.update()

    

class Snake:
    
    snk_obj=None
    direction="up"
    direction_2="up"
    beads=[]
    beads_2=[]
    snk_score=0
    snk2_score=0
    def __init__(self):
        self.snake=turtle.Turtle()
        self.snake.penup()
        self.snake.color("Lime")
        self.snake.shape("square")
        self.snake.direction="Stop"
        Snake.snk_obj=self
        

        self.snake_2=turtle.Turtle()
        self.snake_2.goto(x=50,y=0)
        self.snake_2.penup()
        self.snake_2.color("cyan")
        self.snake_2.shape("square")
        self.snake_2.direction="Stop"
        
        
        
        
        self.snake_binding()
       
        
    def snake_up(self):
        if self.snake.direction!="Down":
            self.snake.direction="Up"

    def snake_down(self):
        if self.snake.direction!="Up":
            self.snake.direction="Down"
        
    
    def snake_left(self):
        if self.snake.direction!="Right":
            self.snake.direction="Left"
    
    def snake_right(self):
        if self.snake.direction!="Left":
            self.snake.direction="Right"
    
    
    
    def snake_2_up(self):
        if self.snake_2.direction!="Down":
            self.snake_2.direction="Up"

    def snake_2_down(self):
        if self.snake_2.direction!="Up":
            self.snake_2.direction="Down"
        
    
    def snake_2_left(self):
        if self.snake_2.direction!="Right":
            self.snake_2.direction="Left"
    
    def snake_2_right(self):
        if self.snake_2.direction!="Left":
            self.snake_2.direction="Right"
    
    
    
    
    def snake_movement(self):
        if self.snake.direction=="Up":
            y=self.snake.ycor()
            self.snake.sety(y+20)
        
        if self.snake.direction=="Down":
            y=self.snake.ycor()
            self.snake.sety(y-20)
        
        if self.snake.direction=="Right":
            x=self.snake.xcor()
            self.snake.setx(x+20)
        
        if self.snake.direction=="Left":
            x=self.snake.xcor()
            self.snake.setx(x-20)
        
        
        if self.snake_2.direction=="Up":
            y=self.snake_2.ycor()
            self.snake_2.sety(y+20)
        
        if self.snake_2.direction=="Down":
            y=self.snake_2.ycor()
            self.snake_2.sety(y-20)
        
        if self.snake_2.direction=="Right":
            x=self.snake_2.xcor()
            self.snake_2.setx(x+20)
        
        if self.snake_2.direction=="Left":
            x=self.snake_2.xcor()
            self.snake_2.setx(x-20)
    
    def snake_binding(self):
        Screen.obj.window.listen()
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_up,"Up")
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_down,"Down")
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_right,"Right")
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_left,"Left")
        
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_2_up,"w")
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_2_down,"s")
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_2_right,"d")
        Screen.obj.window.onkeypress(Snake.snk_obj.snake_2_left,"a")
    
    

  
        
#279  border boundry y
#279 border boundry x
    
class Fruit:
    def __init__(self):
        self.fruit=turtle.Turtle()
        self.fruit.color("red")
        self.fruit.shape("circle")
        self.fruit.penup()
        self.fruit.goto(70,130)
        self.snake_eating_fruit()
    
    def snake_eating_fruit(self):
        Screen.obj.window.update()
        
        self.border_collisons()
        
        if Snake.snk_obj.snake.distance(self.fruit) < 20 :
            
            self.fruit.hideturtle()
            x=random.randint(-299,299)
            y=random.randint(-299,299)
            self.fruit.goto(x,y)
            self.fruit.showturtle()
            Snake.snk_score+=1
            Screen.obj.update_score()
            
            time.sleep(0.001)
            
            
            new_bead=turtle.Turtle()
            new_bead.penup()
            new_bead.color("red")
            new_bead.shape("square")
            Snake.beads.append(new_bead)

            
        if Snake.snk_obj.snake_2.distance(self.fruit) <20:    
        
            self.fruit.hideturtle()
            x=random.randint(-299,299)
            y=random.randint(-299,299)
            self.fruit.goto(x,y)
            self.fruit.showturtle()
            Snake.snk2_score+=1
            
            Screen.obj.update_score()
            
            time.sleep(0.001)
            
            new_bead_2=turtle.Turtle()
            new_bead_2.penup()
            # new_bead_2.hideturtle()
            new_bead_2.color("red")
            new_bead_2.shape("square")
            Snake.beads_2.append(new_bead_2)
        
        self.beads_movement()
        Snake.snk_obj.snake_movement()
        
        Screen.obj.window.ontimer(self.snake_eating_fruit,95)   

    def beads_movement(self):
     
       
        for i in range(len(Snake.beads) - 1, 0, -1):
            x = Snake.beads[i - 1].xcor()
            y = Snake.beads[i - 1].ycor()
            Snake.beads[i].goto(x, y)
        
        
        if Snake.beads:
            x=Snake.snk_obj.snake.xcor()
            y=Snake.snk_obj.snake.ycor()
            
            Snake.beads[0].goto(x,y)
        
        if Snake.beads_2:
            x=Snake.snk_obj.snake_2.xcor()
            y=Snake.snk_obj.snake_2.ycor()
            
            Snake.beads_2[0].goto(x,y)

        for i in range(len(Snake.beads_2) - 1, 0, -1):
            x = Snake.beads_2[i - 1].xcor()
            y = Snake.beads_2[i - 1].ycor()
            Snake.beads_2[i].goto(x, y)
           
            
        
    def border_collisons(self):
        if Snake.snk_obj.snake.xcor() > 280 or Snake.snk_obj.snake.xcor() < -280 or Snake.snk_obj.snake.ycor() > 280 or Snake.snk_obj.snake.ycor() < -280:
            time.sleep(0.4)
            turtle.bye()

        if Snake.snk_obj.snake_2.xcor() > 280 or Snake.snk_obj.snake_2.xcor() < -280 or Snake.snk_obj.snake_2.ycor() > 280 or Snake.snk_obj.snake_2.ycor() < -280:
            time.sleep(0.4)
            turtle.bye()



Screen()



