import random
number = random.randint(1, 20)
attempts = 5
print("="*65)
print("                 Welcome to Number guessing Game")
print("="*65)
print()
print("Type 1 to start the game")
print("Type 2 to know the rules")
print("Type 3 to Exit the Game")
n = int(input())
if n == 1:
    while attempts > 0:
        print("Guess a Number between 1 and 20")
        n1 = int(input())
        if n1 == number:
            print("Congratulations! You guessed the correct number!")
        elif n1<number:
            print("Too low!")
            print("HINT:- Try a higher number.")
        elif n1>number:
            print("Too high!")
            print("HINT:- Try a lower number.")
        else:
            print("Invalid input! Enter a number between 1 and 20.")
        attempts -= 1
        if attempts == 0:
            print("You have no more attempts left!")
elif n ==2:
    print(" The Rules are:")
    print("# You have to choose a number between 1 and 20")
    print("# You have 5 attempts")
    print("# You will get hint after each wrong attempt")
else:
    print("Game Ended")


    