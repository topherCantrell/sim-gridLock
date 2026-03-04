import json

from gridlock import pieces
from itertools import combinations

quick = {}

for k,v in {**pieces.PIECES, **pieces.OTHER_PIECES}.items():
    quick[k] = v.width * v.height    


oks = []

fnd_cnt = 0
def possible_pieces(state, qkeys, area):    
    global fnd_cnt    
    if len(state) <= 4:
        print(">>>", state, fnd_cnt)
    for i in qkeys:
        narea = area + quick[i]
        if narea == 64:
            g = ''.join(sorted(state + i))
            if g not in oks:
                oks.append(g)
                # print(g)
                fnd_cnt += 1
        elif narea < 64:
            nkeys = qkeys.copy()
            nkeys.remove(i)
            possible_pieces(state + i, nkeys, narea)


qkeys = list(quick.keys())
possible_pieces('', qkeys, 0)

print(">>> FOUND: ", fnd_cnt)
with open('possible_pieces.txt', 'w') as f:
    json.dump(oks, f)
