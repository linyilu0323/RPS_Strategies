# "Rock-Paper-Scissors" Strategies



An interesting discussion on RPS strategy:

https://www.nature.com/articles/srep05830

**Main conclusions are:**

1. Rock is more likely to be used in the first round (P_rock = 0.36, P_paper = 0.33, P_scissors = 0.32)
2. Human tend to follow a pattern: if winning, keeping the same; if losing, change.

**The resulting key strategy involves:**

1. Start the game with "paper"
2. Follow "R -> P -> S" pattern if the previous game is either win or lose
3. Follow "S -> P -> R" pattern if the previous game is draw



This repo implemented abovementioned strategy #2 and #3.

Observations:

- If your opponent can really be "random", i.e. `random_choice` - this strategy does not increase your chance of winning.
- If your opponent follows the pattern explained in the paper, i.e. `average_human_choice`, you, i.e. `smart_human_choice` will significantly increase the chance of winning.
- Note that the `average_human_choice` is the statistical behavior of hundreds of players in the study, with hundreds of repeats each player. In real life, the `N_rounds` is a small number (usually < 5), 



Files:

- `rps.py` is used to evaluate two pairs of RPS strategy by repeating the game 1000 times and print the win-lose results.
- `play_smarthuman.py` is an interactive play, it takes your input (0 - rock; 1- paper; 2 - scissors) and you will be competing with the `smart_human_choice` strategy mentioned above for 10 rounds.