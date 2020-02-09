from turtle import *

pencolor("green")
pensize(5)

while True:
    new_direction = input("Give a new direction (l/r): ")
    
    while True:
        try:
            new_angle = int(input("Give me a new angle: "))
            break
        except:
            print("You are stupid.")
    while True:
        try:
            distance = int(input("Give me a distance: "))
            break
        except:
            print ("You've come so far. Don't be stupid again.")
    

    if new_direction == "l":
        left(new_angle)
    elif new_direction == "r":
        right(new_angle)
            
    forward(distance)
