from gridlock import resources

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

folded = {
}

print('Checking solutions for',len(solutions.items()))
keys = list(solutions.keys())
for hh in range(len(keys)):
    k = keys[hh]
    v = solutions[k]
    if(len(v) % 8 != 0):
        raise Exception(f'Invalid number of solutions for {k}')    
    boards = []
    for i in range(len(v)):
        b = v[i]
        boards.append([chr(c) for c in b])       
    for i in range(len(boards)):        
        stats = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        for rots in range(8):
            b = resources.rotate_board(boards[i], rots)                  
            for j in boards:                
                if j == b:
                    stats[rots] += 1                    
        for s in stats.values():
            if s != 1:
                 raise Exception(f'Invalid solution for {k}')  
    folded[k] = []
    for j in boards:
        fnd = False
        for rots in range(8):
            b = resources.rotate_board(j, rots)            
            if b in folded[k]:
                fnd = True
                break
        if not fnd:
                folded[k].append(b)
    print('>>>', hh, k, len(v), len(folded[k]))
            
total_folded = 0
for _, v in folded.items():
    total_folded += len(v)
print('Total folded solutions:', total_folded)

