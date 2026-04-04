from gridlock.gridlock_svg_maker import GridlockSVGMaker
from gridlock.board import Board
from gridlock.pieces import OTHER_PIECES

def svg_pieces():
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

def svg_all_8x8_pieces():

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

def svg_2x3_solution():
    b1 = 'CBCBCA'
    b2 = 'FFFFBB'
    b3 = 'GGGGGG'
    svg = GridlockSVGMaker()
    brd1 = Board(2,3)
    brd1.from_string(b1)   
    brd2 = Board(2,3)
    brd2.from_string(b2)
    brd3 = Board(2,3)
    brd3.from_string(b3) 
    svg.render_boards('./art/two-three.svg', [
        [brd1, '', 'black', True],
        [brd2, '', 'black', True],
        [brd3, '', 'black', True],
    ],1)

def svg_5x3_solution():
    b1 = '''
    EEEEE
    DDDDA
    CCCBB
    '''
    b2 = '''
    KKKKB
    KKKKB
    KKKKA
    '''
    b3 = '''
    IIIII
    IIIII
    EEEEE
    '''
    b4 = '''
    RRRRR
    RRRRR
    RRRRR
    '''
    svg = GridlockSVGMaker()
    brd1 = Board(5,3)
    brd1.from_string(b1)    
    brd2 = Board(5,3)
    brd2.from_string(b2)
    brd3 = Board(5,3)
    brd3.from_string(b3)
    brd4 = Board(5,3)
    brd4.from_string(b4)
    svg.render_boards('./art/five-three.svg', [
        [brd1, '', 'black', True],
        [brd2, '', 'black', True],
        [brd3, '', 'black', True],
        [brd4, '', 'black', True],
    ],1)

def svg_12x12_solution():
    b1 ='''
    CCCTTTTTTTII
    GGGTTTTTTTII
    GGGTTTTTTTII
    OOOOOOKKKKII
    OOOOOOKKKKII
    EEEEEAKKKKPP
    SSSSSSHHHHPP
    SSSSSSHHHHPP
    SSSSSSDDDDPP
    JJJRRRRRFFPP
    JJJRRRRRFFPP
    JJJRRRRRBBPP
    '''
    svg = GridlockSVGMaker()
    brd1 = Board(12,12)
    brd1.from_string(b1)    
    svg.render_boards('./art/twelve.svg', [
        [brd1, '', 'black', True],
    ],1)

if __name__ == "__main__":
    svg_pieces()
    svg_all_8x8_pieces()
    svg_5x3_solution()
    svg_2x3_solution()
