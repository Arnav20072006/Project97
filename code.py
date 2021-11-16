import random
print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number in beetween 1 and 9!")
while chances < 5:
    guess = int(input("Enter your guess ->"))
    if guess == number:
        print("Congratulations, you won!")
    elif guess < number:
        print("Your guess was too low, guess a higher number!",guess)
    else:
        print("Your guess was too high, guess a lower number!",guess)
    chances +=1
if not chances < 5 :
    print("You lost! The number was",number)