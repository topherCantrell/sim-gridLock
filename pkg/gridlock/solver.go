package gridlock

import (
	"fmt"
	"os"
)

var total_sols int = 0

// Check if the board is a winning board (i.e. all pieces are on the board). If
// it is, print the solution and increment the total_sols counter.
// If a file is provided, write the solution to the file instead of printing it.
func checkForWin(brd *Board, file *os.File) {
	if brd.CountValue('.') == 0 {
		total_sols += 1
		if file != nil {
			file.Write(brd[:])
		} else {
			fmt.Println("Found solution:")
			brd.Print()
		}
	}
}

// Public interface to solve the board. Returns the total number of solutions found.
// If a file is provided, writes the solutions to the file instead of printing them.
func Solve(brd *Board, file *os.File) int {
	total_sols = 0
	solve_recursive(brd, file)
	return total_sols
}

// Recursive helper function to run one piece from upper left to lower right
// at both rotations.
func solve_recursive(brd *Board, file *os.File) {

	// Find the largest piece that isn't on the given board
	fnd := -1
	for i, p := range Pieces {
		if brd.CountValue(p.Name) == 0 && brd.CountValue(p.Name|32) == 0 {
			fnd = i
			break
		}
	}
	if fnd < 0 {
		// All pieces are on the board
		return
	}
	piece := Pieces[fnd]

	// Slide and rotate the piece over the board

	for rot := range 2 {
		if rot == 1 && (piece.Width == piece.Height) {
			// Square pieces are the same no matter the rotation. We
			// can save time by skipping rotations on a square piece.
			continue
		}
		for y := range 8 {
			for x := range 8 {
				if brd.PlacePiece(piece, x, y, rot == 1) {
					checkForWin(brd, file)
					solve_recursive(brd, file)
				}
				brd.RemovePiece(piece)
			}
		}
	}

}
