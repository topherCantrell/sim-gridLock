from gridlock import resources

class Board:

    def __init__(self):
        self.board = ['.']*64

    def from_bytes(self, b):
        self.board = [chr(c) for c in b]
    
    def to_bytes(self):
        return bytes([ord(c) for c in self.board])    

    def place_piece(self, piece, x, y, rot):
        width = piece[1]
        height = piece[2]
        letter = piece[0]
        if rot:
            width, height = height, width
            letter = letter.lower()
        for j in range(height):
            if y+j >= 8:
                return False
            for i in range(width):
                if x+i >= 8:
                    return False
                pos = (y+j)*8 + x + i
                if self.board[pos] != '.':
                    return False
                self.board[pos] = letter
        return True
        

    def remove_piece(self, piece):
        for i in range(64):
            if self.board[i] == piece[0].upper() or self.board[i] == piece[0].lower():
                self.board[i] = '.'

    def rotate(self, num_rotations):
        ret = self.board[:]
        if num_rotations >= 4:
            # Mirror first                       
            for y in range(8):
                for x in range(8):
                    ret[y*8+x] = self.board[(7-y)*8 + x]
            num_rotations -= 4
        while num_rotations > 0:
            scratch = ret[:]
            for y in range(8):
                for x in range(8):
                    a = scratch[(7-x)*8 + y]
                    if a not in 'AFJ':
                        if a.isupper():
                            a = a.lower()
                        else:
                            a = a.upper()
                    ret[8*y + x] = a
            num_rotations -= 1        
        b = Board()
        b.board = ret
        return b
            

    def print(self):
        for i in range(8):
            print(''.join(self.board[i*8:(i+1)*8]))

if __name__ == "__main__":
    b = Board()
    b.place_piece(resources.PIECES['K'], 0, 0, True)
    b.print()
    print()
    c = b.rotate(5)
    c.print()
        