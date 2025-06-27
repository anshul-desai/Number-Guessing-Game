import random
number_to_guess = random.randint(1, 100)

count = 0
while count < 10:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess > number_to_guess:
        print("Too high! Try again")
        count = count + 1
    elif guess < number_to_guess:
        print("Too low! Try again")
        count = count + 1
    else:
        count = count + 1
        print("Congratulations! You guessed it in " + str(count) + " attempts!")
        break

if count == 10:
    print("Game over! Better luck next time!")
