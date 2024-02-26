import string
import random

character = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def genrate_password():
  password_length = int(input("How long would you like your password to be? "))
  random.shuffle(character)

  password = []

  for x in range(password_length):
    password.append(random.choice(character))

  random.shuffle(character)


  password = "".join(password)

  print(password)

option = input("Do you want to password a generate? (yes/no)")

if option == "yes":
  genrate_password()
elif option == "no":
  print("program ended")
  quit()
else:
  print("invlid value")
  quit()
