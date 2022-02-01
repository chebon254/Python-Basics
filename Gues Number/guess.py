import random


def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess agin. Too low.")
        elif guess > random_number:
            print("Sorry, guess again, too high")

    print("Yah! Congratulation. You have guessed correctly!")


def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c'  and low != high:
        guess = random.randint(low, high)
        feedback = input(f"If {guess} too high (H), too loo (L), or correct (C)??").lower();
        if feedback == 'h':
            high = guess - 1;
        if feedback == 'l':
            low = guess + 1;
    print("Yah! The computer guessed number, {guess} correctly!")

comp_guess(10)