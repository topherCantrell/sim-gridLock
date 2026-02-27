
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
