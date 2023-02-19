# Write your code here
import random

win_matrix_template = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

playable_hands = list()
stats = list()

human_name = input("Enter your name:")
print(f"Hello, {human_name}")

with open("rating.txt", "r") as f:
    for line in f.readlines():
        if line.startswith(human_name):
            temp_stats = line.split(" ")
            stats.append(temp_stats[0])
            stats.append(int(temp_stats[1]))
            break
    if human_name not in stats:
        stats.append(human_name)
        stats.append(0)

    user_labeled_playable_hands = input()  # Has to be seperated by a comma
    if user_labeled_playable_hands != "":
        win_matrix = dict()
        for sign in user_labeled_playable_hands.split(","):
            playable_hands.append(sign)

        for sign in playable_hands:
            win_matrix[sign] = win_matrix_template[sign]
    else:
        win_matrix = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}
        playable_hands = ("rock", "paper", "scissors")

    print("Okay, let's start")
    while True:
        human_play_hand = input()

        if human_play_hand == "!exit":
            print("Bye!")
            break
        elif human_play_hand == "!rating":
            print(f"Your rating: {stats[1]}")
            continue
        elif human_play_hand not in playable_hands:
            print("Invalid input")
            continue

        computer_play_hand = playable_hands[random.randint(0, len(playable_hands) - 1)]

        if human_play_hand == computer_play_hand:
            print(f"There is a draw ({computer_play_hand})")
            stats[1] += 50
        elif human_play_hand in win_matrix[computer_play_hand]:
            print(f"Sorry, but the computer chose {computer_play_hand}")
        else:
            print(f"Well done. The computer chose {computer_play_hand} and failed")
            stats[1] += 100
