import random #imports the ramdom library to use the ramdom.randint function

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize a variable to keep track of the player's guess None is to show absence of a value or null value 
guess = None

# Use a while loop to repeatedly prompt the player for their guess
while guess != number_to_guess: # returns true if values on either side are not equal therefore continuing loop 
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Too low, try again.")
    elif guess > number_to_guess:
        print("Too high, try again.")
    else:
        print("Congratulations, you guessed the number!")
