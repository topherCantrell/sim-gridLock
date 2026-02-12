
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
    '02:62A13b50c',
    '03:35A24b02C',
    '04:10A67B52C',
    '05:64A25B13c',
    '06:76A65b25c',
    '07:70A41b21c',
    '08:07A21b31C',
    '09:54A35B13C',
    '10:17A23B20c',
    '11:00A20b53c',
    '12:00A20b53C',
    '13:15A50B00C',
    '14:46A41B00C',
    '15:32A56b75c',
    '16:64A13B00C',
    '17:37A34b05c',
    '18:45A63b10C',
    '19:35A45b01C',
    '20:77A24B37C',
    '21:73A43B20C',
    '22:12A54B20C',

    '23:35A23b45C',
    '24:56A45b52C',
    '25:24A50B00C',
    '26:36A42b70c',
    '27:50A24B01c',
    '28:05A00b30c',
    '29:43A00b42C',
    '30:52A30B13C',
    '31:33A50B43c',
    '32:42A02b53C',
    '33:47A32b23c',
    '34:55A50B32c',
    '35:54A05B52C',
    '36:35A20B23C',
    '37:75A50b40c',
    '38:64A37B50c',
    '39:75A20B23C',
    '40:44A23B45C',
    '41:36A04B30c',
    '42:73A50b45c',
    '43:44A31B01C',
    '44:55A31B01C',
]

def place_piece(board, letter, x, y):
    piece = PIECES[letter.upper()]
    if letter.isupper():
        for i in range(piece[1]):
            for j in range(piece[0]):
                pos = (y+i)*8 + j + x
                if board[pos] != '.':
                    return False
                board[pos] = letter
    else:
        for i in range(piece[0]):
            for j in range(piece[1]):
                pos = (y+i)*8 + j + x
                if board[pos] != '.':
                    return False
                board[pos] = letter

def make_board(card):
    board = [
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
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
        print(''.join(board[i*8:(i+1)*8]))
