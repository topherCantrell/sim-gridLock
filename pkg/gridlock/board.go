package gridlock

import (
	"fmt"
	"slices"
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

// Count the number of occurances of a value on the board
func (b *Board) CountValue(val byte) int {
	ret := 0
	for _, v := range b {
		if v == val {
			ret += 1
		}
	}
	return ret
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
		letter = letter | 32 // Make it lowercase
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
	for index, c := range b {
		// Convert to uppercase for compare
		if c&(255-32) == p.Name {
			b[index] = '.'
		}
	}
}

// Make a compact (11 character) representation of the solved board
func (b *Board) CompactSolution() string {
	usedLetters := []byte{}
	ret := []byte{}
	for _, c := range b {
		if !slices.Contains(usedLetters, c) {
			ret = append(ret, c)
			usedLetters = append(usedLetters, c)
		}
	}
	return string(ret)
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
