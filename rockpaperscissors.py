import random

import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


class Player:
    score = 0

    def __init__(self):
        self.my_move_history = []
        self.their_move_history = []

    def learn(self, my_move, their_move):
        self.my_move_history.append(my_move)
        self.their_move_history.append(their_move)


class RockPlayer(Player):
    def move(self):
        return "rock"


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move1 = input("Rock, paper, scissors?>>>\n").lower()
            if move1 in moves:
                return move1
                break
            else:
                print("Invalid input. Try again!")


class ReflectPlayer(Player):
    def move(self):
        if len(self.their_move_history) == 0:
            return random.choice(moves)
        else:
            return self.their_move_history[len(self.their_move_history)-1]


class CyclePlayer(Player):
    def move(self):
        length = len(self.my_move_history)
        if length == 0:
            return random.choice(moves)
        elif length == 1:
            last_move = self.my_move_history[0]
            possible_moves = two_choices(last_move)
            return random.choice(possible_moves)
        else:
            last_two_moves = self.my_move_history[length-2: length]
            remaining_move = one_choice(last_two_moves)
            return remaining_move

# Use for ReflectClass
def two_choices(move):
    if move == "rock":
        return ["paper", "scissors"]
    elif move == "paper":
        return ["scissors", "rock"]
    else:
        return ["paper", "rock"]

# Use for ReflectClass
def one_choice(moves):
    if "rock" in moves and "scissors" in moves:
        return "paper"
    if "paper" in moves and "scissors" in moves:
        return "rock"
    return "scissors"


def print_pause(message):
    print(message)
    time.sleep(1)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player One: {move1}")
        print(f"Player Two: {move2}")
        if move1 == move2:
            print("\n**Tie!**\n")
        elif beats(move1, move2):
            print("\n**Player One Wins!**\n")
            self.p1.score += 1
        else:
            print_pause("\n**Player Two Wins!**\n")
            self.p2.score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("It's time to play rock, paper, scissors!")
        while True:
            try:
                best_of = int(input("How many rounds "
                              "would you like to play?\n"))
                break
            except ValueError:
                print("Please enter a whole number (ex: 1, 5, 17).")
        print_pause(f"Ok! Best of {best_of} rounds.")
        print_pause("Ready, set, play!")
        for round in range(best_of):
            print_pause(f"Round {round+1}:")
            self.play_round()
            print_pause(f"Score:")
            print(f"Player One {self.p1.score}")
            print(f"Player Two {self.p2.score}\n")
        print_pause("GAME OVER!\n")
        print(f"FINAL SCORE:")
        print(f"Player One {self.p1.score}")
        print(f"Player Two {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("**PLAYER ONE WINS!**")
        elif self.p2.score > self.p1.score:
            print("**PLAYER TWO WINS!**")
        else:
            print("**PLAYER ONE AND TWO TIED! CAT'S GAME!**")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
