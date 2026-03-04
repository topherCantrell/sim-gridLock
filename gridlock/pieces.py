
class Piece:    
    def __init__(self, name, width, height, color):
        self.letter = ord(name)
        self.width = width
        self.height = height
        self.color = color

PIECES = {
    'K': Piece('K', 4,3,'yellow'),
    'J': Piece('J', 3,3,'orange'),
    'I': Piece('I', 5,2,'blue'),
    'H': Piece('H', 4,2,'blue'),
    'G': Piece('G', 3,2,'blue'),
    'F': Piece('F', 2,2,'red'),
    'E': Piece('E', 5,1,'green'),
    'D': Piece('D', 4,1,'green'),
    'C': Piece('C', 3,1,'white'),
    'B': Piece('B', 2,1,'white'),
    'A': Piece('A', 1,1,'white'),
}

OTHER_PIECES = {
    '9': Piece('9', 8, 8, 'teal'),
    '8': Piece('8', 8, 7, 'coral'),
    '7': Piece('7', 7, 7, 'coral'),
    '6': Piece('6', 8, 6, 'magenta'),
    '5': Piece('5', 7, 6, 'magenta'),
    '4': Piece('4', 6, 6, 'magenta'),
    '3': Piece('3', 8, 5, 'brown'),
    '2': Piece('2', 7, 5, 'brown'),
    '1': Piece('1', 6, 5, 'brown'),
    '0': Piece('0', 5, 5, 'brown'),
    'Z': Piece('Z', 8, 4, 'pink'),
    'Y': Piece('Y', 7, 4, 'pink'),
    'X': Piece('X', 6, 4, 'pink'),
    'W': Piece('W', 5, 4, 'pink'),
    'V': Piece('V', 4, 4, 'pink'),
    'U': Piece('U', 8, 3, 'gold'),
    'T': Piece('T', 7, 3, 'gold'),
    'S': Piece('S', 6, 3, 'gold'),
    'R': Piece('R', 5, 3, 'gold'),
    'Q': Piece('Q', 8, 1, 'cyan'),
    'P': Piece('P', 7, 1, 'cyan'),
    'O': Piece('O', 6, 1, 'cyan'),
    'N': Piece('N', 8, 2, 'purple'),
    'M': Piece('M', 7, 2, 'purple'),
    'L': Piece('L', 6, 2, 'purple'),
}
