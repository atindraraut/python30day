# this is the 2nd programme of the 30 days challenge
import random

x = "y"
while x =="y":
    no = random.randint(1,6)#generates a random value between 1 and 6

    if no ==1:
        print("-----")
        print("|   |")
        print("| 0 |")
        print("|   |")
        print("-----")
    if no ==2:
        print("-----")
        print("|   |")
        print("|0 0|")
        print("|   |")
        print("-----")
    if no ==3:
        print("-----")
        print("|  0|")
        print("| 0 |")
        print("|0  |")
        print("-----")
    if no ==4:
        print("-----")
        print("|0 0|")
        print("|   |")
        print("|0 0|")
        print("-----")
    if no ==5:
        print("-----")
        print("|0 0|")
        print("| 0 |")
        print("|0 0|")
        print("-----")
    if no ==6:
        print("-----")
        print("|000|")
        print("|000|")
        print("|000|")
        print("-----")

    x = input("enter y to roll again and n to end: ")
    print("\n")