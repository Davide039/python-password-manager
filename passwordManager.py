from string import ascii_letters as letters, digits, punctuation
from random import choice

passwords = {}

file = open("passwords.txt", 'a+')
file.seek(0)
# check if file contains something and if it's the case, add data to passwords
for line in file.readlines():
    passwords[line.split(": ")[0]] = line.split(": ")[1]

# create a generated password and assigns it to a given service
def generatePassword(service):
    if service not in passwords.keys():
        chars = letters + digits + punctuation
        password = ''.join(choice(chars) for _ in range(12))
        passwords[service] = password
        file.write(service + ": " + password + "\n")
    else: print("That password is already in the list\n")

# gets the password of a given service
def getPassword(service):
    print(passwords.get(service, "That password doesn't exist\n"))

# adds a user defined password to a given service
def addPassword(service, password):
    if service not in passwords.keys():
        passwords[service] = password
        file.write(service + ": " + password + "\n")
    else: print("That password already exists. Try with a different service\n")

def viewPasswords():
    for i, item in enumerate(passwords.items()):
        key, value = item
        print(f"{ i + 1 }. { key }: { value }")

# recursive function
def ask():
    # init variables
    service_generate = ""
    service_add = ""
    password = ""
    service_get = ""

    # display the actions
    print("""
    0. Exit the program
    1. Generate a new password
    2. Add a new password
    3. Get an existant password
    4. View all the added passwords\n\n
    """)
    action = int(input("What do you want to do? "))

    # execute code
    if action == 0:
        exit()
    if action == 1:
        service_generate = input("Type the service you want to generate the password for(e.g. Github, Instagram, Youtube...): ")
        generatePassword(service_generate)
        print("The text file was updated\n")
        ask()
    if action == 2:
        service_add = input("Type the service you want to add the password for(e.g. Github, Instagram, Youtube...): ")
        password = input("Now type the password you want to assign to %s: " % service_add)
        addPassword(service_add, password)
        print("The text file was updated\n")
        ask()
    if action == 3:
        service_get = input("Type the service you want to get your password of: ")
        getPassword(service_get)
        ask()
    if action == 4:
        viewPasswords()
        ask()
    else:
        print("Please enter a value between 0 and 3\n")
        ask()
ask()