#Write a program that asks the user how many dice to roll. The program rolls all the dice
# once and prints out the sum of the numbers. Use a for loop.

import random
user = int(input("Enter how many dice to roll: "))
diceset = []
sum = 0
for i in range(int(user)):
    dice_roll = random.randint(1,6)
    diceset.append(dice_roll)
    sum+= dice_roll
    print(diceset)
print(f" the sum of the dice rolled is {sum}")

#Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the
# reverse=True argument.
# Initialize an empty list to store the numbers
numbers = []
while True:
    user = input("Enter a number or an empty string to quit: ")
    if user == "":
        break
    numbers.append(int(user))
numbers.sort(reverse=True)
print("The five greatest numbers are:")
for i in range(min(5,len(numbers))):
    print(numbers[i])

#Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is
# an integer.
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

number =int(input("Enter a integer: "))
if number >1:
    for i in range(2,number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
            print(f"{number} is a prime number.")

else:
    print(f"{number} is not a prime number.")

#Write a program that asks the user to enter the names of five cities one by on (use a for loop
# for reading the names) and stores them into a list structure. Finally, the program prints out
# the names of the cities one by one, one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.

cities = []

for i in range(5):
    city = input("Enter the name of city {}: ".format(i + 1))
    cities.append(city)
print("The cities you entered are:")
for city in cities:
    print(city)
