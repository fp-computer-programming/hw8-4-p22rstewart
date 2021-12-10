# Author RTS 12/9/21

from random import randint

def game(wins = 0, losses = 0, ties = 0, matches = 0):
        """Play rock paper scissors"""
        player = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        computer = randint(0, 2)
        wrong = False

        if not wrong:
            if player == computer:
                print("It's a tie!")
                ties += 1
            elif player == 0:
                if computer == 1:
                    losses += 1
                else:
                    print("You win, rock crushes scissors!\n")
                    wins += 1
            elif player == 1:
                if computer == 2:
                    print("You lose, scissors cuts paper.\n")
                    losses += 1
                else:
                    print("You win, paper covers rock!\n")
                    wins += 1
            elif player == 2:
                if computer == 0:
                    print("You lose, rock crushes scissors.\n")
                    losses += 1
                else:
                    print("You win, scissors cuts paper!\n")
                    wins += 1
            elif player != 0 or player != 1 or player != 2:
                print("You put a number other than rock, paper, or scissors, so another round will start.\n")
                game()
        
        matches += 1
        repeat = input("To play again, enter Y. To stop playing, enter N: ")

        if repeat.lower() == "y":
            game(wins, losses, ties, matches)
        elif repeat.lower() == "n":
            print("Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties) + " Matches: " + str(matches))

game()
