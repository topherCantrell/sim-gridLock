from gridlock.board import Board

print("Loading solutions from file...")
with open('solutions.bin', 'rb') as f:
    solutions = {}
    while True:
        b = f.read(64)
        if not b:
            break
        k = ''
        # All the edges
        for i in range(8):
            k = k + chr(b[0*8 + i])
            k = k + chr(b[7*8 + i])
            k = k + chr(b[i*8 + 0])
            k = k + chr(b[i*8 + 7])
        # Just the corners 
        # k = chr(b[0]) + chr(b[7]) + chr(b[63]) + chr(b[56])
        k = k.upper()
        k = ''.join(sorted(k))
        if k not in solutions:
            solutions[k] = [b]
        else:
            solutions[k].append(b)

n = 0
for k, v in solutions.items():
    n += len(v)
print(f'Loaded {n} solutions from file.')

folded = {}

# There are 8 possible rotations for any board. We expect solutions to come in groups of 8 -- one
# solution for each rotation. We check that here.

print('Checking solutions for',len(solutions.items()))
keys = list(solutions.keys())
for hh in range(len(keys)):
    k = keys[hh]
    v = solutions[k]
    # The total number of solutions must be a multiple of 8
    if(len(v) % 8 != 0):
        raise Exception(f'Invalid number of solutions for {k}')    
    boards = []
    for i in range(len(v)):
        boards.append(Board(v[i]))
    for i in range(len(boards)):        
        stats = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        for rots in range(8):
            b = boards[i].rotate(rots)                  
            for j in boards:                
                if j.grid == b.grid:
                    stats[rots] += 1                    
        for s in stats.values():
            if s != 1:
                 raise Exception(f'Invalid solution for {k}')  
    folded[k] = []
    for j in boards:
        fnd = False
        for rots in range(8):
            b = j.rotate(rots)            
            if b in folded[k]:
                fnd = True
                break
        if not fnd:
                folded[k].append(b)
    # For processing feedback
    print('>>>', hh, k, len(v), len(folded[k]))
            
total_folded = 0
for _, v in folded.items():
    total_folded += len(v)

print(f'Loaded {n} solutions from file.')
print('All solutions are grouped correctly into families of 8 rotations.')
print(f'Total solution families: {total_folded}')
