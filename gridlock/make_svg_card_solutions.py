import json

from gridlock.board import Board
from gridlock.gridlock_svg_maker import GridlockSVGMaker

print("Loading winnable.json...")
with open('winnable.json', 'r') as f:
    winnable = json.load(f)
    print(f'Loaded {len(winnable)} winnable positions from file.')


def svg_card_solutions():
    crds = []
    for rec in winnable:
        if len(rec) > 3:
            crds.append(rec)

    svg = GridlockSVGMaker()

    board_infos = []
    for rec in crds[:22]:
        brd = Board(8,8)
        brd.from_string(rec[2].upper())
        board_infos.append([brd, rec[3], 'green', True])    
    svg.render_boards('./art/solutions01-22.svg', board_infos, 0.5)    

    board_infos = []
    for rec in crds[22:44]:
        brd = Board(8,8)
        brd.from_string(rec[2].upper())
        board_infos.append([brd, rec[3], 'blue', True])    
    svg.render_boards('./art/solutions23-44.svg', board_infos, 0.5)

    board_infos = []
    for rec in crds[44:66]:
        brd = Board(8,8)
        brd.from_string(rec[2].upper())
        board_infos.append([brd, rec[3], 'orange', True])
    svg.render_boards('./art/solutions45-66.svg', board_infos, 0.5)

    board_infos = []
    for rec in crds[66:]:
        brd = Board(8,8)
        brd.from_string(rec[2].upper())
        board_infos.append([brd, rec[3], 'red', True])
    svg.render_boards('./art/solutions67-88.svg', board_infos, 0.5)


if __name__ == "__main__":
    svg_card_solutions()
