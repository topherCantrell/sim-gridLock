import json

from gridlock.gridlock_svg_maker import GridlockSVGMaker
from gridlock.board import Board

def svg_non_winnables():

    NON1 = """
    .A......
    BB......
    ..CCC...
    ........
    ........
    ........
    ........
    ........
    """

    # 3 solutions
    WIN1 = """
    A.......
    BB......
    ..CCC...
    ........
    ........
    ........
    ........
    ........
    """

    SOL1 = """
    AEEEEEFF
    BBDDDDFF
    HHCCCKKK
    HHJJJKKK
    HHJJJKKK
    HHJJJKKK
    IIIIIGGG
    IIIIIGGG
    """

    NON2 = """
    ........
    BB......
    ..CCC...
    ........
    ........
    ........
    ........
    .......A
    """

    svg = GridlockSVGMaker()
    brd1 = Board(8,8)
    brd1.from_string(NON1)
    brd2 = Board(8,8)
    brd2.from_string(WIN1)
    brdS = Board(8,8)
    brdS.from_string(SOL1)
    brd3 = Board(8,8)
    brd3.from_string(NON2)    
    svg.render_boards('./art/unwinnable.svg', [
        [brd1, 'Unwinnable', 'black', True],
        [brd2, 'Winnable', 'black', True],
        [brdS, 'Solution (1 of 3)', 'black', True],
        [brd3, 'Unwinnable', 'black', True],
    ],1)

    P1 = """
    DDDD....
    BBEEEEE.
    ..CCC...
    ........
    ........
    ........
    ........
    .......A
    """

    P2 = """
    EEEEE...
    BBDDDD..
    ..CCC...
    ........
    ........
    ........
    ........
    .......A
    """

    P3 = """
    EEEEEA..
    BBDDDD..
    ..CCC...
    ........
    ........
    ........
    ........
    ........
    """

    brd1 = Board(8,8)
    brd1.from_string(P1)
    brd2 = Board(8,8)
    brd2.from_string(P2)
    brd3 = Board(8,8)
    brd3.from_string(P3)
    svg.render_boards('./art/unwinnableWhy.svg', [
        [brd1, '', 'black', True],
        [brd2, '', 'black', True],
        [brd3, '', 'black', True],
    ],1)


def svg_winnables():  
    most_sols_1 = """
        CCC.....
        ........
        ........
        ........
        ........
        .......B
        .......B
        .......A
    """

    solution_1 = """
        CCCKKKKE
        JJJKKKKE
        JJJKKKKE
        JJJDDDDE
        IIIIIFFE
        IIIIIFFB
        HHHHGGGB
        HHHHGGGA
    """

    most_sols_2 = """
        CCC.....
        ........
        ........
        ........
        ........
        .......A
        .......B
        .......B
    """

    solution_2 = """
        CCCKKKKE
        JJJKKKKE
        JJJKKKKE
        JJJDDDDE
        IIIIIFFE
        IIIIIFFA
        HHHHGGGB
        HHHHGGGB
    """

    # These two starts have 1084 solutions (note they are related with A and B swapped). I would say that
    # THIS is the easiest starting point. But it violates the "exactly one".

    svg = GridlockSVGMaker()
    brd1 = Board(8,8)
    brd1.from_string(most_sols_1)
    brd2 = Board(8,8)
    brd2.from_string(solution_1)  
    svg.render_boards('./art/most1084a.svg', [
        [brd1, '', 'black', True],
        [brd2, '', 'black', True],
    ],1)

    brd3 = Board(8,8)
    brd3.from_string(most_sols_2)
    brd4 = Board(8,8)
    brd4.from_string(solution_2)  
    svg.render_boards('./art/most1084b.svg', [
        [brd3, '', 'black', True],
        [brd4, '', 'black', True],
    ],1)

if __name__ == "__main__":
    svg_non_winnables()
    svg_winnables()        
    