from gridlock.board import Board
from gridlock.cards import CARDS

print("Loading solutions from file...")
with open('solutions.bin', 'rb') as f:
    solutions = []
    while True:
        b = f.read(64)        
        if not b:
            break
        solutions.append(Board(b))
print(f'Loaded {len(solutions)} solutions from file.')

for card in CARDS:        
    for rot in range(8):
        test = card.start_board.rotate(rot)
        for c in CARDS:
            if c.name == card.name:
                continue                
            if test.grid == c.start_board.grid:
                print(f'Error: {card.name} matches {c.name} with rotate {rot}')
print(f'All {len(CARDS)} cards are unique under rotation.')

# TODO make sure all these cards are in abc_positions.json

