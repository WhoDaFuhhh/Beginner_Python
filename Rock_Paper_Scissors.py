import random

print("Lets play a game of Rock, Paper, Scissors.")

   ### Options ###
print('What would you like to select?')
options = ["Rock", "Paper", "Scissors"]
print(options)
   
   ### Player input ###
p1 = str(input())
if p1 == "Rock":
    print("Player 1 selects Rock")
elif p1 == "Paper":
    print("Player 1 selects Paper")
elif p1 == "Scissors":
    print("Player 1 selects Scissors")
else:
    print("Player 1 did not make a valid selection")

     ### Computer input ###
p2 = random.choice(options)
print("Player 2 selects " + str(p2))

    ### Winning conditions ###
if p1 == p2:
    print('Its a tie!')
elif p1 == "Rock" and p2 == "Paper":
    print("Player 1 Wins! Rock beats Paper")
elif p1 == "Rock" and p2 == "Scissors":
    print("Player 2 Wins! Paper beats Scissors")
elif p1 == "Paper" and p2 == "Rock":
    print("Player 2 wins! Rock beats Paper")
elif p1 == "Paper" and p2 == "Scissors":
    print("Player 2 Wins! Scissors beats Paper")
elif p1 == "Scissors" and p2 == "Paper":
    print("Player 1 Wins! Scissors beats Paper!")
elif p1 == "Scissors" and p2 == "Rock":
    print("Player 2 Wins! Rock beats Paper")
