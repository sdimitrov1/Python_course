from random import randint
machine_number = randint(start_number,end_number)

max_tries = 3
start_number  = int(input("Plaese choose the lowest number: "))
end_number = int(input("Plaese choose the highest number: "))

print("I'm thinking about a number, between [{}, {}]. Can you guess it in {} tries?".
    format(start_number, end_number, max_tries))

guessed = False

count_try = 1


while count_try <= max_tries:

    while True:
        guess = int(input("\nTry {}. Enter a number: ".format(count_try)))
        if ( start_number <= guess <= end_number):
            break
        else:
            print("Enter a number in [{}, {}]".format(start_number, end_number))

    if guess == machine_number:
        guessed = True
        break
    elif guess < machine_number:
        print("Your guess is less than my number.")
    else:
        print("Your guess is greater than my number.")

    count_try += 1

if guessed:
    print("You guessed right! {} was my number! And you've guessed it in {} tries!".format(machine_number, count_try))
else:
    print("You didnt guess my number, better luck next time! My number was {}!".format(machine_number))
