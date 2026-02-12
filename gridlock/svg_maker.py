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

    def set_text(self, text, color):
        self.board = self.board.replace('middle"><', f'middle">{text}<')
        self.board = self.board.replace('fill="black"', f'fill="{color}"')
        g = 'style="fill:#808080;stroke:black;stroke-width:2"'
        h = f'style="fill:#808080;stroke:{color};stroke-width:2"'
        self.board = self.board.replace(g, h)

    def set_scale(self, scale):
        i = self.board.find("<!-- TOP -->")
        n = self.board[0:i].replace("scale(1)", f"scale({scale})")
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

    def make_svg(self, fname, boards, scale, with_text=True):     

        spec_height = 135
        if with_text:
            spec_height = 150

        num_rows = 0
        num_cols = 1                

        x,y = 0,0
        for board in boards:
            p = True
            board.set_position(x,y)
            board.set_scale(scale)
            x += 135*scale
            if num_cols < 4:
                num_cols += 1
            if x >= 135*4*scale:
                p = False
                x = 0
                y += spec_height*scale                
                num_rows += 1
                num_cols = 4
        if p:
            num_rows += 1

        width = 135 * num_cols * scale
        height = spec_height * num_rows * scale

        self.template_write = self.template_write.replace(' width="128"', f' width="{width}"')
        self.template_write = self.template_write.replace(' height="150"', f' height="{height}"')

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
    card_boards = []
    for card in resources.CARDS[66:]:
        board = resources.make_board(card)
        b = maker.render_board(board)
        b.set_text(f"{card[:2]}", "red")
        card_boards.append(b)
    
        
    maker.make_svg('test.svg', card_boards, 1, with_text=True)