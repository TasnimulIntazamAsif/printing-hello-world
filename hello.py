import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Hello World")

# Create and set up the turtle
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.color("white")
text_turtle.speed(3)
text_turtle.penup()

# Function to write a single character with animation
def write_char(char, size=40, font_type="Arial"):
    text_turtle.write(char, font=(font_type, size, "bold"))
    text_turtle.forward(size)
    time.sleep(0.2)  # Pause between each character

# Position the turtle to start writing
text_turtle.goto(-150, 0)

# Write "Hello" with animation
hello_text = "Hello,"
for char in hello_text:
    text_turtle.color("cyan")
    write_char(char)

# Move to next line for "World!"
text_turtle.goto(-150, -60)

# Write "World!" with animation
world_text = "World!"
for char in world_text:
    text_turtle.color("magenta")
    write_char(char)

# Add a decorative border
border = turtle.Turtle()
border.hideturtle()
border.color("green")
border.penup()
border.goto(-200, 50)
border.pendown()
border.speed(5)

# Draw a rectangular border
for _ in range(2):
    border.forward(400)
    border.right(90)
    border.forward(150)
    border.right(90)

screen.mainloop() 