# number1=input("Please enter number 1")
# number2=input("Pease enter divisor ")
# try:
#     val = int(number1)/ int(number2)
#     print(val)
# except (ZeroDivisionError,ValueError):
#     print ("sd")
import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("This is final clause which always excutes")

first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)

