
PIECES = {
    'A': (1,1,'white'),
    'B': (2,1,'white'),
    'C': (3,1,'white'),
    'D': (4,1,'green'),
    'E': (5,1,'green'),
    'F': (2,2,'red'),
    'G': (3,2,'blue'),
    'H': (4,2,'blue'),
    'I': (5,2,'blue'),
    'J': (3,3,'orange'),
    'K': (4,3,'yellow'),
}

CARDS = [
    '01:17A46b32C',
    '02:35A24b02C',
]

def place_piece(board, letter, x, y):
    piece = PIECES[letter.upper()]
    if letter.isupper():
        for i in range(piece[1]):
            for j in range(piece[0]):
                pos = (y+i)*8 + j + x
                if board[pos] != 0:
                    return False
                board[pos] = letter
    else:
        for i in range(piece[0]):
            for j in range(piece[1]):
                pos = (y+i)*8 + j + x
                if board[pos] != 0:
                    return False
                board[pos] = letter

def make_board(card):
    board = [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
    ]

    card = card[3:]
    for i in range(0, len(card), 3):
        letter = card[i+2]        
        x = int(card[i])
        y = int(card[i+1])
        place_piece(board, letter, x, y)        

    return board

def print_board(board):
    for i in range(8):
        for j in range(64):
            if board[j] == 0:
                board[j] = '.'
        print(''.join(board[i*8:(i+1)*8]))
