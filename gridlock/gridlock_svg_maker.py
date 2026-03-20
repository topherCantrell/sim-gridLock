import pathlib
from gridlock.svg_maker import SVGMaker
from gridlock.board import Board
import pathlib
from gridlock.pieces import PIECES, OTHER_PIECES
from gridlock.cards import CARDS

class GridlockSVGMaker:
      
    def __init__(self):
        script_dir = pathlib.Path(__file__).parent.resolve()
        self.maker = SVGMaker(f"{script_dir}/template.svg")

    def render_board(self, brd, text, color, bx, by, scale, show_piece_text=False):
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
            pieces += piece
        
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
            brd = self.render_board(board_info[0], board_info[1], board_info[2], px, py, scale, board_info[3])
            brds += brd
            nc += 1
            px += one_width+gap
            if nc>=4:
                nc = 0
                nr += 1
                px = 5
                py += one_height+gap

        height = py+one_height+gap

        if len(board_infos)>4:
            width = 4*(one_width+gap)+2*scale-gap
        else:
            width = len(board_infos)*(one_width+gap)+2*scale-gap
           
        root = self.maker.make_part('FILE', WIDTH=width, HEIGHT=height-gap, BOARDS=brds)

        with open(fname, 'w') as f:
            f.write(root)

def report_given():
    b1 = '''
    GGGJJJHH
    GGGJJJHH
    CCCJJJHH
    IIDDDDHH
    IIBEEEEE
    IIBAKKKK
    IIFFKKKK
    IIFFKKKK
    '''

    b2 = '''
    JJJIIIII
    JJJIIIII
    JJJDKKKK
    EHHDKKKK
    EHHDKKKK
    EHHDFFGG
    EHHAFFGG
    ECCCBBGG
    '''

    svg = GridlockSVGMaker()
    brd1 = Board(8,8)
    brd1.from_string(b1)
    brd2 = Board(8,8)
    brd2.from_string(b2)
    svg.render_boards('./art/given.svg', [
        [brd1, 'Shipped', 'black', False],
        [brd2, 'Imprinted', 'black', False],
    ],1)

def report_unsolvable():
    b1 = '''
    .BB.....
    CCC.A...
    ........
    ........
    ........
    ........
    ........
    ........
    '''
    
    svg = GridlockSVGMaker()
    brd1 = Board(8,8)
    brd1.from_string(b1)    
    svg.render_boards('./art/unsolvable.svg', [
        [brd1, 'Unsolvable', 'black', True],
    ],1)

def report_card_sampler():
    svg = GridlockSVGMaker()
    board_infos = [
        [CARDS[0].start_board, CARDS[0].name, 'green', True],
        [CARDS[22].start_board, CARDS[22].name, 'blue', True],
        [CARDS[44].start_board, CARDS[44].name, 'orange', True],
        [CARDS[66].start_board, CARDS[66].name, 'red', True],

    ]
    # for card in CARDS:
    #     board_infos.append([card.start_board, card.name, 'black', False])
    svg.render_boards('./art/card_samples.svg', board_infos, 1)

def report_pieces():
    b1 = '''
    A.BB.CCC
    ........
    ........
    DDDD....
    ........
    ........
    EEEEE...
    ........
    '''

    b2 = '''
    FF...GGG
    FF...GGG
    ........
    HHHH....
    HHHH....
    ........
    IIIII...
    IIIII...
    '''

    b3 = '''
    JJJ.....
    JJJ.....
    JJJ.....
    ........
    KKKK....
    KKKK....
    KKKK....
    KKKK....
    '''

    svg = GridlockSVGMaker()
    brd1 = Board(8,8)
    brd1.from_string(b1)
    brd2 = Board(8,8)
    brd2.from_string(b2)
    brd3 = Board(8,8)
    brd3.from_string(b3)
    svg.render_boards('./art/pieces.svg', [
        [brd1, '1 High', 'black', True],
        [brd2, '2 High', 'black', True],
        [brd3, '3 High', 'black', True],
    ],1)

def report_all_8x8_pieces():

    for piece in OTHER_PIECES.values():
        piece.color = 'lightgray'

    b1 = '''
    ABBCCCDDDDEEEEELLLLLLMMMMMMMNNNNNNNN
    .FFGGGHHHHIIIIIOOOOOOPPPPPPPQQQQQQQQ
    .FFGGGHHHHIIIIIOOOOOOPPPPPPPQQQQQQQQ
    ...JJJKKKKRRRRRSSSSSSTTTTTTTUUUUUUUU
    ...JJJKKKKRRRRRSSSSSSTTTTTTTUUUUUUUU
    ...JJJKKKKRRRRRSSSSSSTTTTTTTUUUUUUUU
    ......VVVVWWWWWXXXXXXYYYYYYYZZZZZZZZ
    ......VVVVWWWWWXXXXXXYYYYYYYZZZZZZZZ
    ......VVVVWWWWWXXXXXXYYYYYYYZZZZZZZZ
    ......VVVVWWWWWXXXXXXYYYYYYYZZZZZZZZ
    ..........00000111111222222233333333
    ..........00000111111222222233333333
    ..........00000111111222222233333333
    ..........00000111111222222233333333
    ..........00000111111222222233333333
    ...............444444555555566666666
    ...............444444555555566666666
    ...............444444555555566666666
    ...............444444555555566666666
    ...............444444555555566666666
    ...............444444555555566666666
    .....................777777788888888
    .....................777777788888888
    .....................777777788888888
    .....................777777788888888
    .....................777777788888888
    .....................777777788888888
    .....................777777788888888
    ............................99999999
    ............................99999999
    ............................99999999
    ............................99999999
    ............................99999999
    ............................99999999
    ............................99999999
    ............................99999999    
    '''
    
    svg = GridlockSVGMaker()
    brd1 = Board(36,36)
    brd1.from_string(b1)    
    svg.render_boards('./art/possible-pieces.svg', [
        [brd1, 'All Possible 8x8 Pieces', 'black', True],
    ],1)


if __name__ == '__main__':

    # report_given()
    # report_unsolvable()
    # report_card_sampler()
    # report_pieces()
    report_all_8x8_pieces()
    
