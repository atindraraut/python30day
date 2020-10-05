import random
import math
# Taking Inputs
lower = int(input("Enter the lower limit: ")) 

# Taking Inputs
upper = int(input("Enter the upper limit: ")) 

# generating random number between
# the lower and upper are the arguments

x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

# count will start with zero every time
count = 0

""" for calculation of minimum number of
 guesses depends upon range"""
while count < math.log(upper - lower + 1, 2):
	count += 1
	
	# taking guessing number as input
	guess = int(input("Guess a number:- ")) 
	
	# Condition testing
	if x == guess: 
	    print("Congratulations you did it in ", count, " try")
	    # Once guessed, loop will break 
	    break
	elif x > guess:
	    print("You guessed too small!")
	elif x < guess:
	    print("You Guessed too high!")

# If  you guess more the the allotted no of times
 
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d"%x)
    print("\tBetter Luck Next time!")

