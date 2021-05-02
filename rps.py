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

# play the game between two strategies
# input: # of rounds
# output: # of rounds Player1 wins
def play_game(N_rounds):
    prev_choice_player1 = 0
    prev_choice_player2 = 0
    prev_res = 0
    total_win = 0
    total_draw = 0
    total_lose = 0
    for i in range(N_rounds):
        # player1_choice = random_choice()
        player1_choice = smart_human_choice(prev_choice_player1, prev_res)
        # player1_choice = incr_choice(prev_choice_player1)
        # player1_choice = smart_human_choice(prev_choice_player1, prev_res)
        player2_choice = average_human_choice(prev_choice_player2, -prev_res)
        # player2_choice = decr_choice(prev_choice_player2)
        # player2_choice = random_choice()
        prev_res = check_decision(player1_choice, player2_choice)
        total_win += (prev_res>0)
        total_draw += (prev_res==0)
        total_lose += (prev_res<0)
        prev_choice_player1 = player1_choice
        prev_choice_player2 = player2_choice
    print("After {} rounds: ".format(N_rounds))
    print("Player1 won {} times, draw {} times, lose {} times".format(total_win, total_draw, total_lose))

if __name__ == "__main__":
    # N_rounds = 0
    # while (N_rounds == 0):
    #     N_rounds = input('How many rounds do you like to play?')
    #     N_rounds = int(N_rounds)
    play_game(1000)
