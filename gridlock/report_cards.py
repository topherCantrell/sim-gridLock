
from gridlock.gridlock_svg_maker import GridlockSVGMaker
from gridlock.board import Board
from gridlock.cards import CARDS
import json

#  0  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30 31
# 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47
# 48 49 50 51 52 53 54 55
# 56 57 58 59 60 61 62 63

bucket1 = [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 
           62, 61, 60, 59, 58, 57, 56, 48, 40, 32, 24, 16, 8]
bucket2 = [9, 10, 11, 12, 13, 14, 22, 30, 38, 46, 54, 53, 52, 51, 50, 49, 41, 33, 25, 17]
bucket3 = [18, 19, 20, 21, 29, 37, 45, 44, 43, 42, 34, 26]
bucket4 = [27, 28, 36, 35]

def _get_rothash_for_board(data):
    ret = ''
    for bucket in [bucket1, bucket2, bucket3, bucket4]:
        g = ''
        for pos in bucket:
            g += data[pos]
        g = g.replace('.','')
        g = ''.join(sorted(g))
        ret += g+':'
    return ret

def report_all_possible_cards():
    
    # We have all possible placements of pieces A, B, and C in "abc_positions.bin". 
    # Make this with: solver.exe abc.txt abc_positions.bin

    # We have all possible solutions in "solutions.bin".
    # Make this with: solver.exe all.txt solutions.bin

    # We check each possible placement of A, B, and C against the solutions. Along the way, if we see
    # a placement that is a rotation of a previous one, we ignore it. If the placement is winnable,
    # we add it to our "winnable.json" collection. If it's not winnable, we add it to our 
    # "non_winnable.json" collection.     

    # possible_starts: {
    #   rothash: [start, start, start,...],
    #   rothash: [start, start, start,...]
    # }
    # original_solutions: {
    #   rothash: {
    #     start: [solution, solution, ...],
    #     start: [solution, solution, ...]
    #   },
    #   rothash: { ... }
    # }

    print("Loading solutions from file and extracting each starting position ...")
    with open('solutions.bin', 'rb') as f:  # Make with: solver.exe all.txt solutions.bin
        possible_starts = {}
        original_solutions = {}
        while True:
            b = f.read(64)                 
            if not b:
                break
            b = b.decode()
            c = b
            for r in 'DEFGHIJK':
                c = c.replace(r, '.')
            hn = _get_rothash_for_board(c)
            if hn not in possible_starts:
                possible_starts[hn] = [c]
                original_solutions[hn] = {}    
            else:
                possible_starts[hn].append(c)                
            if c not in original_solutions[hn]:
                original_solutions[hn][c] = [b]
            else:
                original_solutions[hn][c].append(b)

    cnt = 0
    for k in possible_starts.values():
        if len(k) % 8 !=0:
            print(f'>>> ERROR: bucket with {len(k)} solutions, which is not a multiple of 8.')
        cnt += len(k)
    
    print(f'Loaded {cnt} solutions from file into {len(possible_starts)} hash buckets.')

    # Load all possible placements of pieces A, B, and C. Some of these are not winnable. Some are
    # rotations of others.

    print('Loading abc positions from file...')
    with open('abc_positions.bin', 'rb') as f:  # Make with: solver.exe abc.txt abc_positions.bin
        abc_positions = {}
        while True:
            b = f.read(64)     
            if not b:
                break
            b = b.decode()
            hn = _get_rothash_for_board(b)
            if hn not in abc_positions:
                abc_positions[hn] = [b]
            else:
                abc_positions[hn].append(b)

    cnt = 0
    for k in abc_positions.values():
        if len(k) % 8 !=0:
            print(f'>>> ERROR: bucket with {len(k)} solutions, which is not a multiple of 8.')
        cnt += len(k)

    print(f'Loaded {cnt} starting positions from file into {len(abc_positions)} hash buckets.')
    
    # Start with the given cards. We already have starting boards for them, and we'll use
    # the rotation from the given card. We build a reverse mapping from starting board to
    # card name so we can include the name in the output.
    
    unique_abc_positions = {}
    board_to_card_name = {}
    for card in CARDS:        
        c = card.start_board.data.decode()
        board_to_card_name[c] = card.name
        hn = _get_rothash_for_board(c)
        if hn not in unique_abc_positions:
            unique_abc_positions[hn] = [c]
        else:
            unique_abc_positions[hn].append(c)

    # Run the list of possible starts. Keep one rotation of each.

    bn = 0
    for hn, bucket in abc_positions.items():
        bn += 1
        print(f'Culling bucket {bn} {hn} with {len(bucket)} abc positions...')
        brd = Board(8,8)
        for cb in bucket:            
            brd.from_string(cb)
            fnd = False        
            for rot in range(8):
                test = brd.rotate(rot)
                for tt in unique_abc_positions.get(hn, []):
                    if test.data.decode() == tt:                        
                        fnd = True
                        break
            if not fnd:
                if hn not in unique_abc_positions:
                    unique_abc_positions[hn] = [cb]
                else:  
                    unique_abc_positions[hn].append(cb)

    cnt = 0
    for k in unique_abc_positions.values():        
        cnt += len(k)
    print(f'There are {cnt} unique abc positions in {len(unique_abc_positions)} hash buckets.')

    # Finally, look for each unique abc position in the solutions. If we find it, it's winnable. 
    # We keep 10,000 non-winnable for example. For winnable, we keep the starting position, the 
    # number of solutions, one solution, and the card name (if any).

    non_winnable = [] # Just the starting board
    winnable = [] # starting board, number of solutions, and one solution board  

    for hn, bucket in unique_abc_positions.items():
        print(f'Checking bucket {hn} with {len(bucket)} abc positions for winnables.')
        for cb in bucket:
            if hn in possible_starts and cb in possible_starts[hn]:
                rec = [
                    cb,  # starting board
                    len(original_solutions[hn][cb]),  # number of solutions
                    original_solutions[hn][cb][0],  # one solution
                ]
                if cb in board_to_card_name:
                    rec.append(board_to_card_name[cb])
                winnable.append(rec)                
            else:
                non_winnable.append(cb)

    print(f'Found {len(winnable)} winnable abc positions and {len(non_winnable)} non-winnable abc positions.')
    
    with open('winnable.json', 'w') as f:
        json.dump(winnable, f)
    with open('non_winnable.json', 'w') as f:
        json.dump(non_winnable, f)     
    
    print(f'Found {len(winnable)} winnable abc positions and {len(non_winnable)} non-winnable abc positions.')
    # OUTPUT: Found 13967 winnable abc positions and 59016 non-winnable abc positions.

if __name__ == "__main__": 
    report_all_possible_cards()
