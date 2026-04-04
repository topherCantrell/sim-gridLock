
class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = bytearray([ord('.')]*width*height)

    def from_string(self, s):
        s = s.replace('\n', '')
        s = s.replace(' ', '')
        for i in range(len(s)):
            self.data[i] = ord(s[i])

    def to_string(self):
        return self.data.decode('ascii')

    def get_pieces(self):
        # [(letter, x, y, w, h, rotation)]
        already_seen = set()
        pieces = []
        for j in range(self.height):
            for i in range(self.width):
                c = self.data[j*self.width+i]
                if c != ord('.') and c not in already_seen:
                    already_seen.add(c)
                    letter = chr(c)
                    x1, y1, x2, y2 = i, j, i, j
                    for k in range(j+1, self.height):
                        if self.data[k*self.width+i] == c:
                            y2 = k
                        else:
                            break
                    for k in range(i+1, self.width):
                        if self.data[j*self.width+k] == c:
                            x2 = k
                        else:
                            break
                    w = x2-x1+1
                    h = y2-y1+1        
                    pieces.append((letter, x1, y1, w, h))
        return pieces
    
    def place_piece(self, piece, x, y, rotated):
        w = piece.width
        h = piece.height
        if rotated:
            w, h = h, w
        c = piece.letter
        for j in range(y, y+h):
            if j>=self.height:
                return False
            for i in range(x, x+w):
                if i>=self.width:
                    return False
                self.data[j*self.width+i] = c
        return True
    
    def rotate(self, num_rotations):
        # TODO this needs to be rotate into and respect the board size
        ret = bytearray(self.data)
        if num_rotations >= 4:
            # Mirror first                       
            for y in range(8):
                for x in range(8):
                    ret[y*8+x] = self.data[(7-y)*8 + x]
            num_rotations -= 4
        while num_rotations > 0:            
            scratch = bytearray(ret)
            for y in range(8):
                for x in range(8):
                    a = scratch[(7-x)*8 + y]                    
                    ret[8*y + x] = a
            num_rotations -= 1        
        b = Board(8,8)
        b.data = ret
        return b
