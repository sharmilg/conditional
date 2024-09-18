#Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each
# season to last three months, December being the first month of winter.
def season(month):
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    if month in (12, 1, 2):
        return seasons[0]
    elif month in (3, 4, 5):
        return seasons[1]
    elif month in (6, 7, 8):
        return seasons[2]
    elif month in (9, 10, 11):
        return seasons[3]
month = int(input("Enter the number of the month (1-12): "))
season = season(month)
print(f"This is {season} season.")

#Write a program that asks the user to enter names until he/she enters an empty string. After each name is read
# the program either prints out New name or Existing name depending on whether the name was entered for the first
# time. Finally, the program lists out the input names one by one, one below another in any order. Use the set data
# structure to store the names.

def call():
    name = set()
    while True:
        user_name = input("Enter names or empty string to exit: ")
        if user_name == "":
            break
        if user_name in name:
            print("Existing name")
        else:
            print("New name")
        name.add(user_name)
    print("The list of names entered")
    for user_name in name:
        print(user_name)

call()


#Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks
# the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to
# quit, the program execution ends. The user can choose a new option as many times they want until they choose to
# quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa
# Airport is EFHK. You can easily find the ICAO codes of different airports online.)
def main():
    airports = {}
    while True:
        print("Choose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Exit the program")
        choose = input("Enter your choice: ")
        if choose == "1":
            icao = input("Enter the ICAO code of the airport: ").upper()
            name = input("Enter the name of the airport: ")
            airports[icao] = name
            print(f"Airport {name} with ICAO code {icao} added.")
        elif choose == "2":
            icao = input("Enter the ICAO code of the airport: ").upper()
            if icao in airports:
                print(f"The name of the airport with ICAO code {icao} is {airports[icao]}.")
            else:
                print("Airport not found.")
        elif choose == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
