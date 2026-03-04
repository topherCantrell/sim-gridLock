from gridlock import pieces

ALL_PIECES = {**pieces.PIECES, **pieces.OTHER_PIECES}
keys = list(ALL_PIECES.keys())

quick = {}
for k,v in ALL_PIECES.items():
    quick[k] = v.width * v.height    

sets_of_pieces = []

def use_piece(state='', pos=0, area=0):
    global sets_of_pieces
    for i in range(pos, len(keys)):
        letter = keys[i]
        if letter in state:
            print(">>>", state, "already has", letter)
            raise Exception("Already used piece: " + letter)            
        new_state = state + letter
        new_area = area + quick[letter]
        if new_area == 64:
            print(">>>", new_state)
            sets_of_pieces.append(new_state)
        elif new_area < 64:
            use_piece(new_state, i+1, new_area)
        else:
            pass  # Move on to next letter
    

use_piece()
print(">>> Total sets of pieces:", len(sets_of_pieces))
