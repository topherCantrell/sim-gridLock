import json

from gridlock.gridlock_svg_maker import GridlockSVGMaker
from gridlock.board import Board

print("Loading winnable.json...")
with open('winnable.json', 'r') as f:
    winnable = json.load(f)
    print(f'Loaded {len(winnable)} winnable positions from file.')

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
    report_winnables()        
    