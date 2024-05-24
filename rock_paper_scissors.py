import random
import emoji

rock = emoji.emojize(" rock\U0000270A")
paper = emoji.emojize(" paper\U0001F590")
scissors = emoji.emojize(" scissors\U0000270C")

player_move = input('Choose your weapon! Rock[r], paper[p] or scissors[s]: ')
if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid choice of weapon. Choose again!')

computer_random_choice = random.randint(1, 3)
computer_move = ''
if computer_random_choice == 1:
    computer_move = rock
elif computer_random_choice == 2:
    computer_move = paper
elif computer_random_choice == 3:
    computer_move = scissors

print()
print(f"Computer's choice of weapon is:{computer_move}")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print()
    print("\033[1;32;40m You won the battle! \n")
elif player_move == computer_move:
    print()
    print('Draw!')
else:
    print()
    print("\033[1;31;40m You lose! The computer won the battle! \n")
