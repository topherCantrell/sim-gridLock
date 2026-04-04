import pathlib
from gridlock.svg_maker import SVGMaker
from gridlock.pieces import PIECES, OTHER_PIECES

class GridlockSVGMaker:
      
    def __init__(self):
        script_dir = pathlib.Path(__file__).parent.resolve()
        self.maker = SVGMaker(f"{script_dir}/template.svg")

    def render_board(self, brd, text, color, bx, by, scale, show_piece_text=False, squares=None):        
        all_pieces = PIECES | OTHER_PIECES
        cells = ''
        for j in range(brd.height):
            for i in range(brd.width):
                cell = self.maker.make_part('CELL', X=i*32, Y=j*32)
                cells += cell
        if text:
            text = self.maker.make_part('BOARD_TEXT', X=brd.width*16, Y=brd.height*32+20, TEXT=text, COLOR=color)
        else:
            text = ''            
        pieces = ''
        piece_info = brd.get_pieces()
        for letter, x, y, w, h in piece_info:
            name = f'PIECE_{letter}'
            rot = 0
            if h>w:
                x = x + w
                rot = 90                
            piece = self.maker.make_part(name, X=x*32, Y=y*32, ROTATION=rot, COLOR=all_pieces[letter].color, TEXT_COLOR='black', show_text=show_piece_text)
            pieces += piece+'\n'

        if squares:
            for x,y,w,h,cc in squares:
                square = self.maker.make_part('SQUARE', X=x*32, Y=y*32, WIDTH=w*32, HEIGHT=h*32, COLOR=cc)
                pieces += square
        
        board = self.maker.make_part('BOARD', X=bx, Y=by, WIDTH=brd.width*32+8, HEIGHT=brd.height*32+8,
                                      COLOR=color, CELLS=cells, PIECES=pieces, TEXT=text, SCALE=scale)
        return board
    
    def render_boards(self, fname, board_infos, scale):
        one_width = board_infos[0][0].width*32+8
        one_height = board_infos[0][0].height*32+8

        if board_infos[0][1]:
            one_height += 32

        gap = 32  # between boards -- horizontally and vertically

        one_width *= scale
        one_height *= scale
        gap *= scale

        nc = 0
        nr = 0

        brds = ''

        px = 5
        py = 5                   

        for board_info in board_infos:
            squares = board_info[4] if len(board_info) > 4 else None
            brd = self.render_board(board_info[0], board_info[1], board_info[2], px, py, scale, board_info[3], squares)
            brds += brd
            nc += 1
            px += one_width+gap
            if nc>=4:
                nc = 0
                nr += 1
                px = 5
                py += one_height+gap

        height = py+one_height+gap
        if len(board_infos)%4 ==0:
            height -= one_height+gap

        if len(board_infos)>4:
            width = 4*(one_width+gap)+2*scale-gap
        else:
            width = len(board_infos)*(one_width+gap)+2*scale-gap
           
        root = self.maker.make_part('FILE', WIDTH=width, HEIGHT=height-gap, BOARDS=brds)

        with open(fname, 'w') as f:
            f.write(root)
