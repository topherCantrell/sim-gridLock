package gridlock

import (
	"fmt"
)

// The gridlock game board
type Board [64]byte

// Create a blank board
func CreateBoard() Board {
	return Board{
		'.', '.', '.', '.', '.', '.', '.', '.',
		'.', '.', '.', '.', '.', '.', '.', '.',
		'.', '.', '.', '.', '.', '.', '.', '.',
		'.', '.', '.', '.', '.', '.', '.', '.',
		'.', '.', '.', '.', '.', '.', '.', '.',
		'.', '.', '.', '.', '.', '.', '.', '.',
		'.', '.', '.', '.', '.', '.', '.', '.',
		'.', '.', '.', '.', '.', '.', '.', '.',
	}
}

var scratchBoard Board = CreateBoard()

// Rotate/mirror a given board. The result is stored in the "brd" parameter.
// The "numRotations" parameter specifies the number of 90 degree clockwise rotations to perform,
// followed by a mirror if the number is 4 or greater.
func (b *Board) RotateInto(brd *Board, numRotations int) {
	if numRotations >= 4 {
		// Mirror the board first
		for y := range 8 {
			for x := range 8 {
				brd[y*8+x] = b[(7-y)*8+x]
			}
		}
		numRotations -= 4
	} else {
		// Just copy the board to the output
		copy(brd[:], b[:])
	}
	for numRotations > 0 {
		// Copy the board to a scratch space, then rotate it back into the output
		copy(scratchBoard[:], brd[:])
		for y := range 8 {
			for x := range 8 {
				c := scratchBoard[(7-x)*8+y]
				brd[y*8+x] = c
			}
		}
		numRotations -= 1
	}
}

// Check if board has a piece with the given letter (case-insensitive)
func (b *Board) HasPiece(letter byte) bool {
	for _, c := range b {
		if c == letter {
			return true
		}
	}
	return false
}

// Check if the board has any empty spaces ('.')
func (b *Board) HasEmpty() bool {
	for _, c := range b {
		if c == '.' {
			return true
		}
	}
	return false
}

// Place a piece on the board. Return "false" if the piece doesn't fit
// because it either runs off the board or runs into another piece.
// Important: the placement stops at the first conflict, but part of the
// piece may be left behind. Use "RemovePiece" to clean any whole or
// partial pieces.
func (b *Board) PlacePiece(p Piece, x int, y int, rot bool) bool {
	height := p.Height
	width := p.Width
	letter := p.Name
	if rot {
		// If this is rotated, swap the dimensions
		height, width = width, height
	}
	// Place the grid of letters -- stop on first conflict
	for j := 0; j < height; j++ {
		if (y + j) >= 8 {
			// The Y coordinate is out of bounds
			return false
		}
		for i := 0; i < width; i++ {
			if (x + i) >= 8 {
				// The X coordinate is out of bounds
				return false
			}
			pos := (y+j)*8 + (x + i)
			if b[pos] != '.' {
				// Another piece is already here
				return false
			}
			b[pos] = letter
		}
	}
	// The full piece was placed
	return true
}

// Remove a piece from the board. This removes all of a piece (partial
// or whole) from anywhere on the board.
func (b *Board) RemovePiece(p Piece) {
	v1 := p.Name
	for index, c := range b {
		// Convert to uppercase for compare
		if c == v1 {
			b[index] = '.'
		}
	}
}

// Print a simple ASCII representation of a board
func (b *Board) Print() {
	for index, c := range b {
		fmt.Print(string(c))
		if (index+1)%8 == 0 {
			fmt.Println()
		}
	}
}
