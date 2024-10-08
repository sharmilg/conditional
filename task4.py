#Write a program that uses a while loop to print out all numbers divisible
# by three in the range of 1-1000.
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

#Write a program that converts inches to centimeters until the user inputs
# a negative value. Then the program ends.

while True:
    inches = float(input("Enter inches or ( negative value to terminate): "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters")

#Write a program that asks the user to enter numbers until they enter an empty string
# to quit. Finally, the program prints out the smallest and largest number from the
# numbers it received.

smallest = None
largest = None
while True:
    user = input("Enter a number or empty string to exit: ")
    if user == "":
        break
    number = float(user)
    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

#Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random
numbers = random.randint(1,10)
while True:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess > numbers:
        print("Too high")
    elif guess < numbers:
        print("Too low")
    else:
        print("Correct")
        break

#Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied. The correct username is python and password rules.

a = "python"
b = "rules"
i = 0
while i < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == a and password == b:
        print("Welcome")
        break
    else:
        i = i+1
        print(f"Incorrect username or password.")

if i == 5:
    print("Access denied")

#Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn
# around the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1),
# (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction of
# points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of
# square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value
# of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total
# number of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the
# total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program
# that asks the user how many random points to generate, and then calculates the approximate value of pi using the
# method explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is
# easy to test if a point falls inside circle A by testing if it fulfills the in equation x^2+y^2<1.).

import random
num_points = int(input("Enter the number of random points to generate: "))
inside_circle = 0
counter = 0
while counter < num_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        inside_circle += 1
    counter += 1
pi = 4 * inside_circle / counter
print(f"The approximation of pi using {num_points} random points is: {pi}")
