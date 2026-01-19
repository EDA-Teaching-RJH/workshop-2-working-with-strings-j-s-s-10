import random

def main():
    number = random.randint(1, 10)
    guess = int(input("Guess a number between and including 1 and 10: "))
    if guess == number:
        print("Correct")
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

main()
