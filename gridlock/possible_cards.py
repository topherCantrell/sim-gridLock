from gridlock import resources
from gridlock.board import Board

keeps = set()

def solve(board):
    global keeps
    # Find the largest piece that isn't on the given board
    fnd = None
    for p in resources.PIECES.values():
        if p[0] not in board.board and p[0].lower() not in board.board:
            fnd = p
            break
    if fnd is None:
        # All pieces are on the board
        keeps.add(''.join(board.board))
        return
    
    # Slide and rotate the piece over the board

    for rot in [False, True]:
        if rot and fnd[0] in 'AFJ':
            # Only one orientation for these pieces
            continue
        for y in range(8):
            for x in range(8):
                if board.place_piece(fnd, x, y, rot):
                    if fnd[0] == 'K':
                        print("Placed K at", x, y, "rotated?", rot)
                    # check_for_win(board)
                    solve(board)
                board.remove_piece(fnd)

if __name__ == "__main__":
    b = Board()
    for skip in 'DEFGHIJK':
        del resources.PIECES[skip]
    print("Solving...")
    solve(b)
    print(f"Total cards found: {len(keeps)}")
