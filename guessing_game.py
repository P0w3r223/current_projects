import random
random_number = random.randint(1,10)
guess = None

while random_number != guess:
    if guess == None:
        print("Pick a number between 1 and 10")
        guess = int(input())
    elif guess > random_number:
        print("Too high")
        guess = int(input())
    elif guess < random_number:
        print("Too low")
        guess = int(input())


print(f"You've guessed the correct number: {random_number}")

