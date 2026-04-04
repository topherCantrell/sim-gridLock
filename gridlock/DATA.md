# Data Files

These intermediate data files are not checked into the repo.

## solutions.bin

`solver all.txt solutions.bin`

All solutions with the given 8x8 pieces. Each board is 64 bytes (one byte per cell).
Solutions come in families of 8 rotations -- the resulting file length should be divisible
by 64 x 8.

## abc_positions.bin

`solver abc.txt abc_positions.bin`

All possible placements of pieces A, B, and C for starting positions.
Solutions come in families of 8 rotations -- the resulting file length should be divisible
by 64 x 8.

## winnable.json non_winnable.json

`gridlock.report_cards.report_all_possible_cards`

This report runs all possible starting positions and sorts them into winnable and not-winnable.

The non_winnable.json is a list of starting positions. The winnable.json is a list of records:
  - Starting board
  - Number of solutions
  - An example solution
  - The name of the card (if this matches a card)

## setsolves8x8.txt

`py -m gridlock.report_possible_pieces 8 8 > setsolves8x8.txt`

The number of solutions for each set of possible 8x8 pieces. A valid set of pieces must have
a total area of 64 to match the board. One of the solution boards is given for each
winnable set of pieces.

Each line is a set of pieces. The first field is the set number (line number). The second field
is the set of pieces with letters A-K. The third field is the number of solutions. The forth 
field is the 64 characters of an example solution (or all dots if no solution). The fifth field
is the time it took to solve for the set of pieces.