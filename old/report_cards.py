from gridlock.board import Board
from gridlock.cards import CARDS
import json


print("Loading solutions from file...")
with open('solutions.bin', 'rb') as f:
    solutions = []
    original_solutions = []
    while True:
        b = f.read(64)   
        original_solutions.append(b)     
        if not b:
            break
        c = b.decode()
        for r in 'DEFGHIJKdefghijk':
            c = c.replace(r, '.')        
        solutions.append(c.encode())        
print(f'Loaded {len(solutions)} solutions from file.')

print('Loading abc positions from file...')
with open('abc_positions.bin', 'rb') as f:
    abc_positions = []
    while True:
        b = f.read(64)     
        if not b:
            break           
        abc_positions.append(b)
print(f'Loaded {len(abc_positions)} abc positions from file.')

def report_solutions_per_card():
    # Are there multiple solutions for any game card?
    for card in CARDS:
        cnt = 0
        for board in solutions:
            if board == card.start_board.grid:
                cnt += 1
        print(f'Card {card.name} found {cnt} times in solutions.')

non_winnable = [] # Just the starting board
winnable = [] # starting board, number of solutions, and one solution board

def report_solutions_per_abc_position():    
    not_winnable_count = 0
    pos = 0
    # Start with the given cards
    unique_abc_positions = set()
    toname = {}
    for card in CARDS:
        unique_abc_positions.add(card.start_board)
        toname[card.start_board.to_bytes()] = card.name
    # Add abc positions but only keep one rotation
        pp = 0
    for cb in abc_positions:
        pp += 1
        if pp % 100 == 0:
            print(f'Checked {pp} abc positions for uniqueness...')
        brd = Board(cb)
        fnd = False        
        for rot in range(8):
            test = brd.rotate(rot)
            for tt in unique_abc_positions:
                if test.grid == tt.grid:
                    fnd = True
                    break
        if not fnd:            
            unique_abc_positions.add(brd)
    print(f'Found {len(unique_abc_positions)} unique abc positions under rotation.')    
    # OUTPUT: Found 72983 unique abc positions under rotation. 
    
    for cb in unique_abc_positions:
        card = cb.to_bytes()
        pos += 1
        if pos % 100 == 0:
            print(f'Checked {pos} abc positions...')
        cnt = 0
        sol = None
        for i in range(len(solutions)):
            board = solutions[i]                  
            if board == card:
                cnt += 1
                if sol is None:
                    sol = original_solutions[i]               
        if cnt == 0:
            not_winnable_count += 1
            if len(non_winnable) < 10000:
                non_winnable.append(card.decode())
        else:
            rec = [card.decode(), cnt, sol.decode()]
            nm = toname.get(card, None)
            if nm is not None:
                rec.append(nm)
            winnable.append(rec)   
    with open('winnable.json', 'w') as f:
        json.dump(winnable, f)
    with open('non_winnable.json', 'w') as f:
        json.dump(non_winnable, f)     

    print(f'Found {len(winnable)} winnable abc positions and {not_winnable_count} non-winnable abc positions.')
    # OUTPUT: Found 13967 winnable abc positions and 59016 non-winnable abc positions.

# report_solutions_per_card()

print("STARTING")
nw = report_solutions_per_abc_position()

