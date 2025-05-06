import turtle

def draw_branch(t, branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:
        return

    # Change color and thickness based on depth
    if depth == max_depth:
        t.color("brown")
        t.pensize(10)
    else:
        t.color("green")
        t.pensize(3)

    t.forward(branch_length)

    position = t.position()
    heading = t.heading()

    # Left branch
    t.left(angle_left)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    t.setposition(position)
    t.setheading(heading)

    # Right branch
    t.right(angle_right)
    draw_branch(t, branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)

    t.setposition(position)
    t.setheading(heading)

# Take user input
angle_left = float(input("Enter left branch angle: "))          
angle_right = float(input("Enter right branch angle: "))        
start_length = float(input("Enter starting branch length: "))    
max_depth = int(input("Enter recursion depth: "))               
reduction_factor = float(input("Enter reduction factor: "))      

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()
t.penup()
t.goto(0, -250)
t.setheading(90)  # Point up
t.pendown()

# Draw the tree
draw_branch(t, start_length, angle_left, angle_right, max_depth, reduction_factor)

turtle.done()
