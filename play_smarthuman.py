import random

# make win/lose/draw decision
# inputs are integers: 0-Rock, 1-Paper, 2-Scissors
# output is: +1=Player1 wins; 0=Draw; -1=Player2 wins.
def check_decision(in1, in2):
    if in1 == in2:
        return 0
    elif in1 + in2 == 2:
        return (in1==0) - (in2==0)
    else:
        return (in1>in2) - (in2>in1)

# pick a random choice
def random_choice():
    return random.randint(0, 2)

# incrementing pattern: 0 --> 1 --> 2 --> 0
def incr_choice(prev_choice):
    return (prev_choice+1)%3

# decrementing pattern: 0 --> 2 --> 1 --> 0
def decr_choice(prev_choice):
    return (prev_choice-1)%3

# average-human:
# based on paper study: https://www.nature.com/articles/srep05830
# if win: keep same choice; if lost: follow R->P->S; if draw: pick a random
def average_human_choice(prev_choice, prev_res):
    if prev_res == 0:
        return random_choice()
    elif prev_res > 0:
        return prev_choice
    else:
        return incr_choice(prev_choice)

# smart-human:
# if won or lost: incrementing pattern; if draw: decrementing pattern
def smart_human_choice(prev_choice, prev_res):
    if prev_res != 0:
        return incr_choice(prev_choice)
    else:
        return decr_choice(prev_choice)

# user play the game against smart-human strategy
# user input: 0-2 integer representing R-P-S selection
# output: print user win or lose
player1_win = 0
player2_win = 0
N_rounds = 0
MAX_ROUNDS = 10

while N_rounds < MAX_ROUNDS:

    player1_choice = input("Enter a choice: 0=Rock, 1=Paper, 2=Scissors --> ")
    player1_choice = int(player1_choice)
    if (player1_choice > 2) or (player1_choice < 0):
        player1_choice = player1_choice%3
    N_rounds += 1

    # set below so player2 start with "Paper" in first round
    prev_choice_player2 = 2
    prev_res = 0

    # play against "smart human"
    player2_choice = smart_human_choice(prev_choice_player2, -prev_res)
    prev_res = check_decision(player1_choice, player2_choice)
    prev_choice_player2 = player2_choice

    # output current round result
    choice_str = ["rock", "paper", "scissors"]
    print("Round # {} of {}".format(N_rounds, MAX_ROUNDS))
    print("You selected: " + choice_str[player1_choice] +"; Computer selected: " + choice_str[player2_choice])
    if prev_res == 0:
        print("It's a draw.")
    elif prev_res > 0:
        print("You won!")
    else:
        print("You lose")

    player1_win += (prev_res>0)
    player2_win += (prev_res<0)

print("After {} rounds: ".format(N_rounds))
print("You won {} times; Computer won {} times".format(player1_win, player2_win))
