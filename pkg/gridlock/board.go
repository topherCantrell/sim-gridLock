package gridlock

import (
	"fmt"
)

// The gridlock game board
type Board struct {
	Width  int
	Height int
	Cells  []byte
}

// Create a blank board
func CreateBoard(width int, height int) Board {
	cells := make([]byte, width*height)
	for i := range cells {
		cells[i] = '.'
	}
	return Board{
		Width:  width,
		Height: height,
		Cells:  cells,
	}
}

// var scratchBoard Board

// Rotate/mirror a given board. The result is stored in the "brd" parameter.
// The "numRotations" parameter specifies the number of 90 degree clockwise rotations to perform,
// followed by a mirror if the number is 4 or greater.
//
// Any geometry can be mirrored. Only squares can be rotated.
// func (b *Board) RotateInto(brd *Board, numRotations int) {
// 	if numRotations >= 4 {
// 		// Mirror the board into the output
// 		for y := range b.Height {
// 			for x := range b.Width {
// 				brd.Cells[y*b.Width+x] = b.Cells[(b.Height-1-y)*b.Width+x]
// 			}
// 		}
// 		numRotations -= 4
// 	} else {
// 		// Just copy the board into the output
// 		copy(brd.Cells, b.Cells)
// 	}
// 	for numRotations > 0 && b.Width == b.Height {
// 		// Copy the board to a scratch space, then rotate it back into the output
// 		if scratchBoard.Width != b.Width || scratchBoard.Height != b.Height {
// 			scratchBoard = CreateBoard(b.Width, b.Height)
// 		}
// 		copy(scratchBoard.Cells, brd.Cells)
// 		for y := range b.Height {
// 			for x := range b.Width {
// 				// TODO
// 				c := scratchBoard.Cells[(7-x)*8+y]
// 				brd.Cells[y*8+x] = c
// 			}
// 		}
// 		numRotations -= 1
// 	}
// }

// Check if board has a piece with the given letter (case-insensitive)
func (b *Board) HasPiece(letter byte) bool {
	for _, c := range b.Cells {
		if c == letter {
			return true
		}
	}
	return false
}

// Check if the board has any empty spaces ('.')
func (b *Board) HasEmpty() bool {
	for _, c := range b.Cells {
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
		if (y + j) >= b.Height {
			// The Y coordinate is out of bounds
			return false
		}
		for i := 0; i < width; i++ {
			if (x + i) >= b.Width {
				// The X coordinate is out of bounds
				return false
			}
			pos := (y+j)*b.Width + (x + i)
			if b.Cells[pos] != '.' {
				// Another piece is already here
				return false
			}
			b.Cells[pos] = letter
		}
	}
	// The full piece was placed
	return true
}

// Remove a piece from the board. This removes all of a piece (partial
// or whole) from anywhere on the board.
func (b *Board) RemovePiece(p Piece) {
	v1 := p.Name
	for index, c := range b.Cells {
		// Convert to uppercase for compare
		if c == v1 {
			b.Cells[index] = '.'
		}
	}
}

// Print a simple ASCII representation of a board
func (b *Board) Print() {
	for index, c := range b.Cells {
		fmt.Print(string(c))
		if (index+1)%b.Width == 0 {
			fmt.Println()
		}
	}
}
