

You can use the following methods:
- `robot.check`: checks if a certain relation is true
- `robot.move_gripper`: moves the gripper

If you are unfamiliar with these functions, you can inspect them by typing `robot.check`,
`robot.move_gripper` in the console.

""",
)
[eod] [code]import random
from game import *


def main():
    while True:
        print('Welcome to Rock Paper Scissors')
        choice = get_choice(False)
        if random.randint(0, 2) == 0:
            comp_choice = 'r'
        elif random.randint(0, 2) == 1:
            comp_choice = 'p'
        else:
            comp_choice = 's'
        if choice == 'q':
            break
        elif choice == comp_choice:
            print('It\'s a tie!')
        elif choice == 'r':
            if comp_choice == 'p':
                print('Sorry, the computer chose paper')
            else:
                print('You chose rock, the computer chose scissors, you win!')
        elif choice == 'p':
            if comp_choice == 's':
                print('Sorry, the computer chose scissors')
            else:
                print('You chose paper, the computer chose rock, you win!')
        elif choice == 's':
            if comp_choice == 'r':
                print('Sorry, the computer chose rock')
            else:
                print('You chose scissors, the computer chose paper, you win!')


if __name__ == '__main__':
    main()
[eod] [code]import copy
from collections import Counter


def get_data():
    return """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def main():
    with open('input.txt') as f:
        data = f.readlines()

    data = [int(l) for l in data]
    data = Counter(data)