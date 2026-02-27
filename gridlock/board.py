from gridlock.pieces import PIECES

class Board:
        
    def __init__(self, grid=None):
        if grid is None:
            self.grid = bytearray([ord('.')]*64)
        else:
            self.grid = bytearray(grid)

    def from_bytes(self, b):
        for i in range(64):
            self.grid[i] = b[i]        
    
    def to_bytes(self):
        return bytes(self.grid)

    def place_piece(self, piece, x, y, rot):
        width = piece.width
        height = piece.height        
        letter = piece.letter
        if rot:
            width, height = height, width
            letter = letter | 32  # Convert to lowercase        
        for j in range(height):
            if y+j >= 8:
                return False
            for i in range(width):
                if x+i >= 8:
                    return False
                pos = (y+j)*8 + x + i
                if self.grid[pos] != ord('.'):
                    return False
                self.grid[pos] = letter
        return True
        

    def remove_piece(self, piece):
        a = piece.letter
        b = piece.letter | 32  # Convert to lowercase
        c = ord('.')
        for i in range(64):
            if self.grid[i] == a or self.grid[i] == b:
                self.grid[i] = c

    def rotate(self, num_rotations):
        ret = bytearray(self.grid)
        if num_rotations >= 4:
            # Mirror first                       
            for y in range(8):
                for x in range(8):
                    ret[y*8+x] = self.grid[(7-y)*8 + x]
            num_rotations -= 4
        while num_rotations > 0:            
            scratch = bytearray(ret)
            for y in range(8):
                for x in range(8):
                    a = scratch[(7-x)*8 + y]
                    if a not in [65, 70, 74]: # A, F, J
                        if a < 97:  # Uppercase
                            a = a | 32  # Convert to lowercase
                        else:
                            a = a & ~32  # Convert to uppercase
                    ret[8*y + x] = a
            num_rotations -= 1        
        b = Board(ret)
        return b
            

    def print(self):
        for y in range(8):
             for x in range(8):
                print(chr(self.grid[y*8+x]), end='')
             print()        

if __name__ == "__main__":
    b = Board()
    b.place_piece(PIECES['K'], 0, 0, True)
    b.print()
    print()
    c = b.rotate(4)
    c.print()
        