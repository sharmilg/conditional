#Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish back
# into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42
if length >= size_limit:
    print("The zander meets the size limit you can keep the fish.")
else:
    difference = size_limit-length
    print(f" The zander is {difference:.2f} centimeter below the size limit.")
    print("You must release the fish into the lake.")


#Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written
# description according to the list below. You must use an if/elif/else structure in your solution.
#LUX: upper-deck cabin with a balcony.
#A: above the car deck, equipped with a window.
#B: windowless cabin above the car deck.
#C: windowless cabin below the car deck.
#If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

cabin_class = (input("Enter the cabin classof the cruise ship:LUX, A,B,C :")).upper()
if cabin_class == "LUX":
    print("LUX: Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: Above the car deck,equipped with a window.")
elif cabin_class == "B":
    print("B: Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.
 # first way using if :

year =int(input("Enter the year: "))
if (year%100==0 and year%400==0 ) or (year%4==0):
    print(f"the  year is {year} is a leap year.")
else:
    print(f"the  year is {year} is not a leap year.")

# second way using while:

year = ""
while year !="exit" :
    year = input("Enter the year or type 'exit' to terminate the program.: ")
    if year == "exit":
        break
    year =int(year)
    if (year%100==0 and year%400==0) or (year%4==0):
            print(f" The year {year} is a leap year ")
    else:
            print(f" The year {year} is not a leap year ")


#Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

gender = (input("Enter your biological gender ( male/female): ")).lower()
hemoglobin = int(input("Enter your hemoglobin (hemoglobin): "))
if gender == "male" and 134 <=hemoglobin<=167:
    print(" Your hemoglobin level is normal")
else:
    if gender == "male" and hemoglobin<134:
        print(" Your hemoglobin level is low")
    elif gender == "male" and hemoglobin>167:
        print(" Your hemoglobin level is high")
    if gender == "female" and 117<= hemoglobin<=155:
        print(" Your hemoglobin level is normal")
    elif gender == "female" and hemoglobin<117:
        print(" Your hemoglobin level is low")
    elif gender == "female" and hemoglobin>155:
        print(" Your hemoglobin level is high")


