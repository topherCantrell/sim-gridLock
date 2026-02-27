from gridlock.pieces import PIECES
from gridlock.board import Board

GIVEN_SOLUTIONS = [
    'GJhCiDbEAKF',   # Ships with the game
    'JIdKehFgACB',   # Printed on the case
]

total_sols = 0

def check_for_win(board):
    global total_sols
    # Check if all pieces are on the board
    if board.grid.count(46) == 0: # ord('.')
        total_sols += 1
        # print("Found solution:")
        # board.print()    

def solve(board):
    global total_sols
    total_sols = 0
    _solve_board(board)
    return total_sols

def _solve_board(board):    
    # Find the largest piece that isn't on the given board
    fnd = None
    for p in PIECES.values():
        if p.letter not in board.grid and (p.letter | 32) not in board.grid:        
            fnd = p
            break
    if fnd is None:
        # All pieces are on the board        
        return
    
    # Slide and rotate the piece over the board

    for rot in [False, True]:
        if rot and fnd.letter in [65, 70, 74]: # A, F, J
            # Only one orientation for these pieces
            continue
        for y in range(8):
            for x in range(8):
                if board.place_piece(fnd, x, y, rot):
                    if fnd.letter == ord('K'):
                        print("Placed K at", x, y, "rotated?", rot)
                    check_for_win(board)
                    _solve_board(board)
                board.remove_piece(fnd)

if __name__ == "__main__":
    import datetime
    print(datetime.datetime.now())
    b = Board()
    print("Solving...")
    total = solve(b)
    print(f"Total solutions found: {total}")
    print(datetime.datetime.now())