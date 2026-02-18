from gridlock import resources

total_sols = 0
last_state = ''

SOLUTIONS = set()

def board_to_repr(board):
    ret = ''
    for c in board:
        if c not in ret:
            ret += c
    return ret

def solve_board(board, state, level=0):
    global last_state, total_sols
    if state[:7] != last_state[:7]:
        print(">>>", state)
        last_state = state    
    if '.' not in board:        
        r = board_to_repr(board)
        if r not in SOLUTIONS:
            SOLUTIONS.add(r)
            print(r)
            with open("solution.txt", "a") as f:
                f.write(r + "\n")
            total_sols += 1
    for letter, piece in resources.PIECES.items():
        if letter in board or letter.lower() in board:
            # This piece is already on the board
            continue
        for rot in range(2):
            if rot:
                if letter in 'AFJ':
                    # Only one orientation for these pieces
                    continue
                letter = letter.lower()
            if level == 0:
                print(">>>", letter)

            for y in range(8):
                for x in range(8):
                    if resources.can_place_piece(board, letter, x, y):
                        brd = board[:]
                        resources.place_piece(brd, letter, x, y)
                        solve_board(brd, state+letter, level+1)


brd = resources.make_board('xx:')
brd = resources.make_board(resources.CARDS[0])
# brd = [
#     'A','B','B','C','C','C','F','F',
#     'D','D','D','D','g','g','F','F',
#     'H','H','H','H','g','g','i','i',
#     'H','H','H','H','g','g','i','i',
#     'k','k','k','.','.','.','i','i',
#     'k','k','k','.','.','.','i','i',
#     'k','k','k','.','.','.','i','i',
#     'k','k','k','E','E','E','E','E'
# ]

solve_board(brd, '')
print("Total solutions:", total_sols)


# ABBCCCFF
# DDDDggFF
# HHHHggii
# HHHHggii
# kkkJJJii
# kkkJJJii
# kkkJJJii
# kkkEEEEE

# ABCFDgHikJE
# ABCFDgHikJE

# print(board_to_repr('ABBCCCFFDDDDggFFHHHHggiiHHHHggiiikkkJJJiiikkkJJJiiikkkJJJiiikkkEEEEE'))
