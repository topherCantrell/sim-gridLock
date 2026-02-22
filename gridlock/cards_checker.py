from gridlock import resources

# with open('solutions.bin', 'rb') as f:
#     solutions = {}
#     while True:
#         b = f.read(64)
#         if not b:
#             break
#         k = ''
#         # All the edges
#         for i in range(8):
#             k = k + chr(b[0*8 + i])
#             k = k + chr(b[7*8 + i])
#             k = k + chr(b[i*8 + 0])
#             k = k + chr(b[i*8 + 7])
#         # Just the corners 
#         # k = chr(b[0]) + chr(b[7]) + chr(b[63]) + chr(b[56])
#         k = k.upper()
#         k = ''.join(sorted(k))
#         if k not in solutions:
#             solutions[k] = [b]
#         else:
#             solutions[k].append(b)
# n = 0
# for k, v in solutions.items():
#     n += len(v)
# print(f'Loaded {n} solutions from file.')

def check_rotates():
    # Make sure all cards are unique under rotation
    card_boards = []
    for card in resources.CARDS:
        board = resources.make_board(card)
        card_boards.append((card, board))        

    for c,b in card_boards:
        for rot in range(8):
            test = b.rotate(rot)
            for ct, bt in card_boards:
                if test.board == bt.board:
                    if c != ct:
                        print(f'Error: {c} matches {ct} with rotate {rot}')

check_rotates()