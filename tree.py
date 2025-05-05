import turtle  # For drawing graphics

# Recursive function to draw the tree
def draw_tree(branch_length, left_angle, right_angle, depth, factor):
    if depth == 0:
        return  # Stop recursion when depth is 0

    # Draw main branch
    turtle.forward(branch_length)

    # Save current position and angle
    position = turtle.position()
    heading = turtle.heading()

    # Draw left branch
    turtle.left(left_angle)
    draw_tree(branch_length * factor, left_angle, right_angle, depth - 1, factor)

    # Return to previous position and angle
    turtle.penup()
    turtle.setposition(position)
    turtle.setheading(heading)
    turtle.pendown()

    # Draw right branch
    turtle.right(right_angle)
    draw_tree(branch_length * factor, left_angle, right_angle, depth - 1, factor)

    # Return to original position and heading after drawing both branches
    turtle.penup()
    turtle.setposition(position)
    turtle.setheading(heading)
    turtle.pendown()

# Take user input for tree parameters
left_angle = int(input("Enter left branch angle (in degrees): "))
right_angle = int(input("Enter right branch angle (in degrees): "))
start_length = float(input("Enter starting branch length (e.g. 100): "))
depth = int(input("Enter recursion depth (e.g. 5): "))
reduction_factor = float(input("Enter length reduction factor (e.g. 0.7): "))

# Setup turtle window and initial position
turtle.speed("fastest")  # Make drawing faster
turtle.left(90)  # Point turtle upward
turtle.penup()
turtle.goto(0, -250)  # Move turtle to bottom center of screen
turtle.pendown()

# Draw the recursive tree
draw_tree(start_length, left_angle, right_angle, depth, reduction_factor)

# Wait for user to close the window
turtle.done()
