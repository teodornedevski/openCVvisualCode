import turtle

turtle.color('red', 'yellow')
turtle.begin_fill()

def Draw (elements[]):
    for i in elements.length() :
        if elements[i] == "circle":
            turtle.left(20)
            if elements [i+1] == "up":
                turtle.forward(10)
            elif elements [i+1] == "back":
                turtle.back(10)
            elif elements [i+1] == "left":
                turtle.left(10)
            else:
                turtle.right(10)
        elif elements[i] == "triangle":
            turtle.speed(300)
            if elements [i+1] == "up":
                turtle.forward(10)
            elif elements [i+1] == "back":
                turtle.back(10)
            elif elements [i+1] == "left":
                turtle.left(10)
            else:
                turtle.right(10)
        elif elements[i] == "square":
            turtle.tilt(30)
            if elements [i+1] == "up":
                turtle.forward(10)
            elif elements [i+1] == "back":
                turtle.back(10)
            elif elements [i+1] == "left":
                turtle.left(10)
            else:
                turtle.right(10)
        else:

            if elements [i+1] == "up":
                turtle.forward(10)
            elif elements [i+1] == "back":
                turtle.back(10)
            elif elements [i+1] == "left":
                turtle.left(10)
            else:
                turtle.right(10)