#Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write a
# main program that rolls the dice until the result is 6. The main program should print out the result of each roll.

import random
def roll():
    score = random.randint(1, 6)
    return score
result = 0
while result != 6:
    result = roll()
    print(f"The dice rolled: {result}")


#Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function
# you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in
# the main program continues until the program gets the maximum number on the dice, which is asked from the user at the
# beginning.

import random

def dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    attempt = 0
    while True:
        roll = dice(sides)
        attempt += 1
        print(f"The dice rolled for {attempt} and got {roll}")
        if roll == sides:
            print(f"You rolled the maximum number! {sides}")
            break

if __name__ == "__main__":
    main()

#Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion
# must be done by using the function. Conversions continue until the user inputs a negative value.

def conversion(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter the volume in gallons (negative value to quit): "))
        if gallons < 0:
            print("Program quited")
            break
        liters = conversion(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")
main()

#Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the
# list. For testing, write a main program where you create a list, call the function, and print out the value it returned.

def addme(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]
result = addme(numbers)
print(f"The sum of the list {numbers} is {result}.")


#Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the
# same as the original list except that all uneven numbers have been removed. For testing, write a main program where
# you create a list, call the function, and then print out both the original as well as the cut-down list.

def remove_odd_numbers(numbers):
    remove_odd_numbers =[]
    for number in numbers:
        if number % 2 == 0:
            remove_odd_numbers.append(number)
    return remove_odd_numbers

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = remove_odd_numbers(original_list)

print(f"Original list:{original_list}")
print(f"List without odd numbers:{list}")


#Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza
# in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the
# user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money
# (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

import math

def calculate_unit_price(diameter, price):

    radius = (diameter / 2) / 100
    area = math.pi * (radius ** 2)
    unit_price = price / area
    return unit_price

diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))

diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))
unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)
print(f"Unit price of the first pizza: {unit_price1:.2f} euros per square meter")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros per square meter")
if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
elif unit_price1 > unit_price2:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")



