import json

from gridlock.gridlock_svg_maker import GridlockSVGMaker
from gridlock.board import Board

from gridlock.cards import CARDS

print("Loading winnable.json...")
with open('winnable.json', 'r') as f:
    winnable = json.load(f)
    print(f'Loaded {len(winnable)} winnable positions from file.')

def wins_per_card():
    """
        Run the list of 88 cards. For each card, find the starting board in the winnable list, and count how many solutions it has. 
        We expect each card to have exactly 1 solution. If any card has 0 or more than 1 solution, report the problem.
    """
    num_problems = 0  
    for card in CARDS:        
        c = card.start_board.data.decode()
        fnd = 0
        for rec in winnable:
            if rec[0] == c:
                fnd += 1
                if rec[1] != 1:
                    print(f'### Card {card.name} has {rec[1]} solutions.')
                    num_problems += 1
                break
        if fnd != 1:
            print(f'### Card {card.name} has {fnd} matches.')
            num_problems += 1
    if num_problems == 0:
        print('All cards have exactly 1 solution.')

def report_winnables():

    # 1: 1850    1850 starting positions have exactly 1 solution.
    # 2: 2326
    # 3: 933
    # 4: 1213
    # ...
    # 787: 2
    # 832: 4
    # 983: 4
    # 1084: 2    2 starting positions have 1084 solutions.

    # Example winnable position with 1084 solutions:
    # ['CCC............................................B.......B.......A', 1084, 'CCCKKKKEJJJKKKKEJJJKKKKEJJJDDDDEIIIIIFFEIIIIIFFBHHHHGGGBHHHHGGGA']
    # Example winnable position with 1084 solutions:
    # ['CCC............................................A.......B.......B', 1084, 'CCCKKKKEJJJKKKKEJJJKKKKEJJJDDDDEIIIIIFFEIIIIIFFAHHHHGGGBHHHHGGGB']

    counts = {}
    for rec in winnable:
        c = rec[1]
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
        if  c == 1084:
            print("Example winnable position with 1084 solutions:")
            print(rec)

    print("Solution counts per winnable position:")
    for c in sorted(counts.keys()):
        print(f'{c}: {counts[c]}')        

if __name__ == "__main__":    
    # report_winnables()        
    wins_per_card()
    