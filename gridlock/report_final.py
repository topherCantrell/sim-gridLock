import json

# from gridlock.cards import CARDS
# from gridlock.svg_maker import SVGMaker
from gridlock.board import Board
from gridlock.svg_maker import SVGMaker

print("Loading winnable.json...")
with open('winnable.json', 'r') as f:
    winnable = json.load(f)
    print(f'Loaded {len(winnable)} winnable positions from file.')

counts = {}
for rec in winnable:
    c = rec[1]
    if c not in counts:
        counts[c] = 0
    counts[c] += 1
    if rec[1] == 1084:
        print("Example winnable position with 1084 solutions:")
        print(rec)

print("Solution counts per winnable position:")
for c in sorted(counts.keys()):
    print(f'{c}: {counts[c]}')


maker = SVGMaker()

crds = []
for rec in winnable:
    if len(rec) > 3:
        crds.append(rec)

boards = []
for rec in crds[:22]:
    brd = Board(rec[2].encode())
    b = maker.render_board(brd)
    b.set_text(f"{rec[3]}", "green")
    boards.append(b)
maker.make_svg('solutions01-22.svg', boards, 1, with_text=True)

boards = []
for rec in crds[22:44]:
    brd = Board(rec[2].encode())
    b = maker.render_board(brd)
    b.set_text(f"{rec[3]}", "blue")
    boards.append(b)
maker.make_svg('solutions23-44.svg', boards, 1, with_text=True)

boards = []
for rec in crds[44:66]:
    brd = Board(rec[2].encode())
    b = maker.render_board(brd)
    b.set_text(f"{rec[3]}", "orange")
    boards.append(b)
maker.make_svg('solutions45-66.svg', boards, 1, with_text=True)

boards = []
for rec in crds[66:]:
    brd = Board(rec[2].encode())
    b = maker.render_board(brd)
    b.set_text(f"{rec[3]}", "red")
    boards.append(b)
maker.make_svg('solutions67-88.svg', boards, 1, with_text=True)

#     board = resources.make_board(card)
#     
#     b.set_text(f"{card[:2]}", "red")
#     card_boards.append(b)


# 
# How many possible cards are there?
# What makes one card harder than another?
# 

