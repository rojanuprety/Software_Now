import turtle

# Recursive function to draw tree
def draw_branch(length, depth, left_angle, right_angle, factor):
    if depth == 0:
        return
    turtle.forward(length)
    
    # Draw left branch
    turtle.left(left_angle)
    draw_branch(length * factor, depth - 1, left_angle, right_angle, factor)
    
    # Return to main branch
    turtle.right(left_angle + right_angle)
    
    # Draw right branch
    draw_branch(length * factor, depth - 1, left_angle, right_angle, factor)
    
    # Return to original heading and position
    turtle.left(right_angle)
    turtle.backward(length)

# User input
left_angle = float(input("Enter left branch angle (degrees): "))
right_angle = float(input("Enter right branch angle (degrees): "))
start_length = float(input("Enter starting branch length (pixels): "))
depth = int(input("Enter recursion depth: "))
reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7): "))

# Setup turtle
turtle.speed('fastest')
turtle.left(90)  # Point upward
turtle.up()
turtle.goto(0, -250)
turtle.down()
turtle.color("green")

# Draw tree
draw_branch(start_length, depth, left_angle, right_angle, reduction_factor)

# Exit on click
turtle.done()
