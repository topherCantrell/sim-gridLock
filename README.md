# At a Glance

Here are some quick facts about the "Rubik's Grid Lock" universe. A detailed discussion follows.

Here are the [solutions to all 88 cards.](SOLUTIONS.md)

There are 1,977,968 ways to fit every piece on the board. Solutions come in groups
of eight rotations (see discussion). 1,977,968 / 8 = 247,246 rotationally-unique solutions.

There are 583,864 ways to place pieces A, B, and C to start a challenge. 583,864 / 8 =
72,983 rotationally-unique starting points. Of these, only 13,967 starting positions
are winnable.

Out of 13,967 possible start-position cards, the game only includes 88. All of the given cards have exactly 1 solution. There are 1,850 cards that have exactly 1 solution. Many cards have multiple solutions. (Two of the cards have 1,084 solutions.)

There are four levels of challenges (22 cards in each level). I have yet to determine what makes one card harder than any other.

The game ships with 11 pieces, but there are 36 [possible unique pieces](art/possible-pieces.svg) for an 8x8 board.

These 36 pieces can be grouped into 28,725 sets of pieces whose areas total 64 (the board's area). But only 17,385 of these sets have solutions. Many sets like WVLJFECA have just 8 solutions (1 family of solutions). Set NMLIHGFEDCBA has the most pieces (12) and the most solutions (5,324,896).

There are lots of sets with 11 pieces, but the given set ABCDEFGHIJK has the 2nd most solutions: 1,977,968.

There are other possible board dimensions. For instance, a 5x3 board has 18 winnable sets of pieces. The set ABCDE has the most solutions of any set, with 40. Set GFCB is in second place with 32.

# Rubik's Grid Lock

![](art/gridlock.jpg)

The game board is an 8x8=64 cell grid. There are 11 unique pieces of various sizes that are placed on the board. There are 88 challenge cards. Each card shows the starting board with  A, B, and C placed on the board. You must fit all the other pieces onto that starting board.

Here are the 11 pieces. I assigned each piece a letter for discussion here and for modeling in the code:

<!-- SVG pieces
A.BB.CCC EE...FFF JJJ.....
........ EE...FFF JJJ.....
........ ........ JJJ.....
DDDD.... GGGG.... ........
........ GGGG.... ........
........ ........ KKKKK...
EEEEE... HHHHH... KKKKK...
........ HHHHH... KKKKK...
-->
![](art/pieces.svg)

The first 3 pieces -- A, B, and C -- are the "fixed" pieces shown on the 88 cards. Every card shows the position of these three pieces and no other piece.

There are 5 pieces with a height of 1 cell: A, B, C, D, and E. There are 4 pieces that are 2 cells high: F, G, H, and I. And there are 2 pieces, J and K, that are 3 cells high.

8 of the pieces have 2 forms: the one shown in the picture above and another rotated 90 degrees. The pieces A, F, and J are square; they have only one form as shown.

# Given Solutions

When you unwrap the game for the first time, the pieces are arranged on the board
in the first solution first solution below. The second solution is imprinted on 
the inside of the case.

![](art/given.svg)

# Challenge Cards

There are 88 cards. See the complete list here: [all cards](CARDS.md)

There are four levels of 22 cards each, from easy to hard. Here is one card from each difficulty level:

![](art/card_samples.svg)

All the cards use pieces A, B, and C. Is this all the possible cards? If not, how many are there?

It is easy to find an unsolvable starting position. You create a 1x1 hole and put the 1x1 piece elsewhere on the board. For instance:

![](art/unsolvable.svg)

The example proves that there are more than 88 possible starting positions and that not all are solvable.

The A piece has 64 possible positions (each square on the board). The B piece has 7x8x2 = 112 possible positions (remember the rotations). The C piece has 6x8x2 = 96 positions. If we allow the pieces to overlap, we have 64x112x96 = 688,128 as an upper bound on the number of possible cards. But we don't allow overlaps.

The code in [gridlock/possible_cards.py] generates all legal combinations (no overlaps) of pieces A, B, and C. There are 583, 864 possible starting points – possible cards. To figure out how many of these are solvable, we'll need code to solve a board.

# All Solutions

The solver algorithm is simple:
  - Find a piece that is not on the board
  - Try to place that piece at all possible X,Y on the board
  - If the piece fits at X,Y:
    - If there are no blank spaces remaining on the board, note the solution
    - Call the solver algorithm recursively for the new board
  - If the piece fits or doesn't fit: keep going with this piece for all possible X,Y
  - Repeat for all pieces on the board

I wrote the solver in Go for performance: [cmd/solver/main.go]. The program takes an input text file that gives the starting board and the list of possible pieces.

I ran the program with a blank starting board and the 11 given pieces to find all possible solutions. It took just under a minute to find all 1,977,968 possible solutions to the game. The program writes the solutions to a binary file for later processing. This 126M binary file is NOT checked into the repo.

# Rotations and Mirroring

TODO to here

TODO talk about rotation/duplicate checker code

When you find a solution, you can rotate the board four times to get a total of four
solutions that are technically unique. You can also take a mirror image of the board
and make four more rotations. Every solution is thus a family of 8 solutions when you
apply rotations and mirroring.

The solver finds all possible solutions without filtering out rotated/mirrored solutions.
We expect the total number of found solutions to be a multiple of 8, which it is. The number of
solution "families" is 1,977,968 / 8 = 247,246. If you memorize these 250K solutions, you can
quickly generate all 2 million possible solutions with a mirror and rotations. That should
impress your friends!

# All Possible Cards

All the cards are rotationally unique as checked by [gridlock/cards_checker.py](gridlock/cards_checker.py).

It is easy to recover the starting board from a solution: just remove all pieces but A, B, and C and
filter out duplicates. The 1,977,968 solutions reduce to 32,528 starting points -- starting cards. When you
remove rotations and duplicates.

TODO: From here down

How many possible cards are there? How many of those possible are solvable?

TODO: Show a few of the not-obvious non-winnable starting points

TODO: Number of solutions for each card. Does this indicate the difficulty? What makes one card "harder" 
than another?

# All Possible Pieces

![](art/possible-pieces.svg)

A set of pieces must:
  - equal the area of the board (64)
  - have at least one solution

TODO there are 28,725 sets of pieces that total 64

TODO count the solutions for each piece set

```
   PIECES        NUM-SOL   EXAMPLE-SOL

----- Sorted by number of pieces in set:
('NMLIHGFEDCBA', 5324896, 'NNNNNNNNMMMMMMMDLLLLLLADIIIIIFFDIIIIIFFDHHHHGGGBHHHHGGGBEEEEECCC')
('KJIHGFEDCBA',  1977968, 'KKKKJJJCKKKKJJJCKKKKJJJCIIIIIGGGIIIIIGGGHHHHDDDDHHHHAFFBEEEEEFFB')
('LKJIHFEDCBA',   368416, 'LLLLLLAEKKKKJJJEKKKKJJJEKKKKJJJEIIIIIFFEIIIIIFFBHHHHCCCBHHHHDDDD')
('NKJIGFEDCBA',   905856, 'NNNNNNNNKKKKJJJCKKKKJJJCKKKKJJJCIIIIIGGGIIIIIGGGFFEEEEEAFFDDDDBB')
('MLKJIGFDCBA',   258792, 'MMMMMMMALLLLLLFFKKKKBBFFKKKKJJJCKKKKJJJCDDDDJJJCIIIIIGGGIIIIIGGG')
('NLKJIFEDCBA',   425792, 'NNNNNNNNLLLLLLADKKKKJJJDKKKKJJJDKKKKJJJDIIIIIFFBIIIIIFFBEEEEECCC')
('MLKJHGFEDBA',   324032, 'MMMMMMMELLLLLLAEKKKKJJJEKKKKJJJEKKKKJJJEHHHHGGFFHHHHGGFFDDDDGGBB')
('NLKJHGFECBA',   434544, 'NNNNNNNNLLLLLLBBKKKKJJJCKKKKJJJCKKKKJJJCHHHHFFGGHHHHFFGGEEEEEAGG')
('NMKJHGFDCBA',   568752, 'NNNNNNNNMMMMMMMCKKKKJJJCKKKKJJJCKKKKJJJAHHHHGGFFHHHHGGFFDDDDGGBB')
('NLKJHGEDCBA',  1161632, 'NNNNNNNNLLLLLLADKKKKJJJDKKKKJJJDKKKKJJJDHHHHGGGBHHHHGGGBEEEEECCC')
...
('4QO',  8, '444444OO444444OO444444OO444444OO444444OO444444OOQQQQQQQQQQQQQQQQ')
('3QN', 12, '3333333333333333333333333333333333333333QQQQQQQQQQQQQQQQNNNNNNNN')
('2TN',  8, '2222222N2222222N2222222N2222222N2222222NTTTTTTTNTTTTTTTNTTTTTTTN')
('1SQ',  8, '111111QQ111111QQ111111QQ111111QQ111111QQSSSSSSQQSSSSSSQQSSSSSSQQ')
('0UR',  8, '00000RRR00000RRR00000RRR00000RRR00000RRRUUUUUUUUUUUUUUUUUUUUUUUU')
('ZUN', 12, 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZUUUUUUUUUUUUUUUUUUUUUUUUNNNNNNNN')
('8N',   4, '88888888888888888888888888888888888888888888888888888888NNNNNNNN')
('6Q',   4, '666666666666666666666666666666666666666666666666QQQQQQQQQQQQQQQQ')
('3U',   4, '3333333333333333333333333333333333333333UUUUUUUUUUUUUUUUUUUUUUUU')
('9',    1, '9999999999999999999999999999999999999999999999999999999999999999')

----- Sorted by number of solutions:
('NMLIHGFEDCBA', 5324896, 'NNNNNNNNMMMMMMMDLLLLLLADIIIIIFFDIIIIIFFDHHHHGGGBHHHHGGGBEEEEECCC')
('KJIHGFEDCBA',  1977968, 'KKKKJJJCKKKKJJJCKKKKJJJCIIIIIGGGIIIIIGGGHHHHDDDDHHHHAFFBEEEEEFFB')
('RLIHGFEDCBA',  1227224, 'RRRRRGGGRRRRRGGGRRRRRBBELLLLLLAEIIIIIFFEIIIIIFFEHHHHCCCEHHHHDDDD')
('PMIHGFEDCBA',  1220328, 'PPPPPPPCPPPPPPPCMMMMMMMCIIIIIGGGIIIIIGGGHHHHDDDDHHHHAFFBEEEEEFFB')
('NLKJHGEDCBA',  1161632, 'NNNNNNNNLLLLLLADKKKKJJJDKKKKJJJDKKKKJJJDHHHHGGGBHHHHGGGBEEEEECCC')
('MLKIHGEDCBA',  1106448, 'MMMMMMMALLLLLLBBKKKKHHHHKKKKHHHHKKKKDDDDIIIIIGGGIIIIIGGGEEEEECCC')
('NKJIGFEDCBA',   905856, 'NNNNNNNNKKKKJJJCKKKKJJJCKKKKJJJCIIIIIGGGIIIIIGGGFFEEEEEAFFDDDDBB')
('OJIHGFEDCBA',   878680, 'OOOOOOFFOOOOOOFFJJJIIIIIJJJIIIIIJJJHHHHBGGGHHHHBGGGEEEEEDDDDCCCA')
('RNLIGFEDCBA',   876880, 'RRRRRGGGRRRRRGGGRRRRRCCCNNNNNNNNLLLLLLADIIIIIFFDIIIIIFFDEEEEEBBD')
('NMKIHFEDCBA',   833920, 'NNNNNNNNMMMMMMMAKKKKHHHHKKKKHHHHKKKKDDDDIIIIIFFBIIIIIFFBEEEEECCC')
...
('5QL', 8, '5555555L5555555L5555555L5555555L5555555L5555555LQQQQQQQQQQQQQQQQ')
('5PN', 8, '5555555N5555555N5555555N5555555N5555555N5555555NPPPPPPPNPPPPPPPN')
('4QO', 8, '444444OO444444OO444444OO444444OO444444OO444444OOQQQQQQQQQQQQQQQQ')
('2TN', 8, '2222222N2222222N2222222N2222222N2222222NTTTTTTTNTTTTTTTNTTTTTTTN')
('1SQ', 8, '111111QQ111111QQ111111QQ111111QQ111111QQSSSSSSQQSSSSSSQQSSSSSSQQ')
('0UR', 8, '00000RRR00000RRR00000RRR00000RRR00000RRRUUUUUUUUUUUUUUUUUUUUUUUU')
('8N',  4, '88888888888888888888888888888888888888888888888888888888NNNNNNNN')
('6Q',  4, '666666666666666666666666666666666666666666666666QQQQQQQQQQQQQQQQ')
('3U',  4, '3333333333333333333333333333333333333333UUUUUUUUUUUUUUUUUUUUUUUU')
('9',   1, '9999999999999999999999999999999999999999999999999999999999999999')
```

# TODO different size boards

The set-solver program takes the dimensions of the board and allowed pieces as arguments.

a 5x3 board has 18 winnable sets of pieces. The set ABCDE has the most solutions of any set, with 40. Set GFCB is in second place with 32.

2x2 board -- just the one soltuion wiht the 2x2 piece (F)

2x3 board -- the 2x3 piece and BF and ABC.

Run stats for 5x5 and 6x5. Note the "possible pieces" can be extracted from all-sets dump.

Adding one to the square dimensions add that many pieces. For instance, we know 8x8 has 36 pieces. Bumping that to 9x9 adds another column on the end of figure??. It adds 9 pieces. 10x10 would add ten more. And so on.

TODO add 19 lowercase letters and stats for 10x10.

max possible in my one-byte-cell model is 1+2+3+...+21+22 = 253 pieces -- 22x22.

