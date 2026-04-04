from gridlock.gridlock_svg_maker import GridlockSVGMaker
from gridlock.board import Board
from gridlock.cards import CARDS

def svg_card_sampler():
    svg = GridlockSVGMaker()
    board_infos = [
        [CARDS[0].start_board, CARDS[0].name, 'green', True],
        [CARDS[22].start_board, CARDS[22].name, 'blue', True],
        [CARDS[44].start_board, CARDS[44].name, 'orange', True],
        [CARDS[66].start_board, CARDS[66].name, 'red', True],

    ]
    svg.render_boards('./art/card_samples.svg', board_infos, 1)  

def svg_cards():
    svg = GridlockSVGMaker()
    card_sets = [
        [0, 22, 'green'],
        [22, 44, 'blue'],
        [44, 66, 'orange'],
        [66, 88, 'red'],
    ]
    for start, end, color in card_sets:
        board_infos = []
        for i in range(start, end):
            board_infos.append([CARDS[i].start_board, CARDS[i].name, color, True])
        ss = str(start+1).rjust(2,'0')
        fn = f'./art/cards{ss}-{end}.svg'
        svg.render_boards(fn, board_infos, 0.5)    

def svg_given():
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

def svg_unsolvable():
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

def svg_rotations():
    b1 = '''
    AMMMMMMM
    88888888
    88888888
    88888888
    88888888
    88888888
    88888888
    88888888
    '''

    svg = GridlockSVGMaker()
    brd1 = Board(8,8)
    brd1.from_string(b1)    
    brd2 = brd1.rotate(1)
    brd3 = brd1.rotate(2)
    brd4 = brd1.rotate(3)
    brd5 = brd1.rotate(6)
    brd6 = brd1.rotate(5)
    brd7 = brd1.rotate(4)
    brd8 = brd1.rotate(7)
    svg.render_boards('./art/rotations.svg', [
        [brd1, '0:', 'black', True],
        [brd2, '1: CW 90', 'black', True],
        [brd3, '2: CW 180', 'black', True],
        [brd4, '3: CW 270', 'black', True],
        [brd5, '4: Mirrored', 'black', True],
        [brd6, '5: CW 90, Mir', 'black', True],
        [brd7, '6: CW 180, Mir', 'black', True],
        [brd8, '7: CW 270, Mir', 'black', True],
    ],1)    

if __name__ == "__main__":
    svg_given()
    svg_unsolvable()
    svg_rotations()
    svg_card_sampler()
    svg_cards()
    