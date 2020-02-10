import random

answer = random.randint(1, 21)

print ('Welcome! To pass the gate you must guess the correct number')
print ('I will give you a hint') 
print ('I am thinking of a number beetween 1 and 20')
print ('You have 5 guesses.')

##Player Ready Response



##Guesses Taken
for guessesTaken in range(6):
        guess = int(input())
        if guess > answer:
            print('That number is too high')
        elif guess < answer:
            print ('That number is too low')
        else:
            break
if guess == answer:
    print ('Good job! You guessed the right number. Come on in for a smoke')
else:
        print (('Nope no weed for you! The correct number is ') + str(answer))