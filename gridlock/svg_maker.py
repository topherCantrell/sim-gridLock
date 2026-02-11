import pathlib
from gridlock import resources

class SVGBoard:
    def __init__(self, board):
        self.board = board

    def place_piece(self, letter, x, y):
        p = resources.PIECES[letter.upper()]
        alt = letter.islower()
        fnd = f"{p[0]}x{p[1]}"
        if alt:
            fnd += "_vert"
        i = self.board.find(f"<!-- {fnd}")
        j = self.board.find("-->", i)
        n = self.board[i:j].replace("translate(0,0)", f"translate({x*16},{y*16})")                
        self.board = self.board[:i] + n + self.board[j:]
        self.board = SVGMaker.uncomment(self.board, fnd)        

    def set_scale(self, scale):
        i = self.board.find("<!-- TOP -->")
        n = self.board[0:i].replace("scale(0)", f"scale({scale})")
        self.board = n + self.board[i:]

    def set_position(self, x, y):
        i = self.board.find("<!-- TOP -->")
        n = self.board[0:i].replace("translate(0,0)", f"translate({x},{y})")
        self.board = n + self.board[i:]


class SVGMaker:

    @staticmethod
    def uncomment(template, s):
        i = template.find(f"<!-- {s}")
        if i<0:
            raise ValueError(f"Cannot find {s} in template")
        i = i + len(f"<!-- {s}")
        j = template.find("-->", i)
        return template[:i] + ' -->'+template[i:j] + template[j+3:]

    def __init__(self):
        script_dir = pathlib.Path(__file__).parent.resolve()
        with open(f"{script_dir}/template.svg", "r") as f:
            self.template = f.read()

        i = self.template.find("<!-- COPY_BEGIN -->")
        j = self.template.find("<!-- COPY_END -->")
        self.template_board = self.template[i + len("<!-- COPY_BEGIN -->"):j].strip()
        self.template_write = self.template[:i + len("<!-- COPY_BEGIN -->")] + self.template[j:]
        
    def make_board(self):
        return SVGBoard(self.template_board)    

    def make_svg(self, fname, boards, scale):        

        num_rows = 1
        num_cols = len(boards)
        if len(boards) > 7:
            num_rows = 2
            num_cols = 7        

        width = 135 * num_cols * scale
        height = 135 * num_rows * scale

        self.template_write = self.template_write.replace(' width="128"', f' width="{width}"')
        self.template_write = self.template_write.replace(' height="128"', f' height="{height}"')

        x,y = 0,0
        for board in boards:
            board.set_position(x,y)
            board.set_scale(scale)
            x += 135*scale
            if x >= 135*7*scale:
                x = 0
                y += 135*scale

        w = self.template_write.replace("<!-- OTHERS -->", "\n".join(board.board for board in boards))
        with open(fname, "w") as f:
            f.write(w)

    def render_board(self, board):
        ret = self.make_board()
        placed = set()
        for i in range(64):
            if board[i] != '.' and board[i] not in placed:
                letter = board[i]                
                ret.place_piece(letter, i%8, i//8)
                placed.add(letter)

        return ret

if __name__ == "__main__":
    maker = SVGMaker()

    tb = [
        'J','J','J','I','I','I','I','I',
        'J','J','J','I','I','I','I','I',
        'J','J','J','d','K','K','K','K',
        'e','h','h','d','K','K','K','K',
        'e','h','h','d','K','K','K','K',
        'e','h','h','d','F','F','g','g',
        'e','h','h','A','F','F','g','g',
        'e','C','C','C','B','B','g','g',
    ]

    tb2 = [
        'G','G','G','J','J','J','h','h',
        'G','G','G','J','J','J','h','h',
        'C','C','C','J','J','J','h','h',
        'i','i','D','D','D','D','h','h',
        'i','i','b','E','E','E','E','E',
        'i','i','b','A','K','K','K','K',
        'i','i','F','F','K','K','K','K',
        'i','i','F','F','K','K','K','K',
    ]

    b0 = maker.render_board(tb2)
    b1 = maker.render_board(tb)
        
    maker.make_svg('test.svg', [b0,b1], 1)