
# Challenge 1


def challenge1(firstname, lastname):
    return lastname, firstname


print(challenge1("Bailey", "Phaphone"))

print()

# Challenge 3


def triangle_formula(b, h):
    return(b * h)**(1/2)


print("Area of triangle=")
print(triangle_formula(3,8))

print()

# Challenge 4


def number(integer):
    if integer > 0:
        return "The number is a positive"
    elif integer < 0:
        return "The number is a negative"
    elif integer == 0:
        return "The number is neither positive or negative"


The_number = number(3)
print(The_number)

print()

# Challenge 5


def circle(r):
    return(r**2)*3.14


print("Area of circle=")
print(circle(4))

# Challenge 6


def sphere(f):
    return(f**3)*4/3*3.14



