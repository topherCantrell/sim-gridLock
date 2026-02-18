package main

import (
	"fmt"

	"github.com/topherCantrell/sim-gridLock/pkg/gridlock"
)

var total_sols int = 0

func solve(brd *gridlock.Board, index uint) {

	// If there are no dots, we have a winner
	fnd := false
	for i := range 64 {
		if brd[i] == '.' {
			fnd = true
			break
		}
	}
	if fnd == false {
		fmt.Println("Solution found:")
		brd.Print()
		total_sols++
		return
	}

	var piece gridlock.Piece
	var letter byte

	// Skip over any rotation of the same piece that is already on the board
	for {
		// We've run out of pieces -- done here
		if index >= uint(len(gridlock.Pieces)) {
			return
		}
		piece = gridlock.Pieces[index]
		letter = piece.Name
		found := false
		for i := range 64 {
			if brd[i] == letter&223 || brd[i] == letter|32 {
				found = true
				break
			}
		}
		if found {
			index++
		} else {
			break
		}
	}

	for i := range 64 {
		if brd[i] == letter&223 || brd[i] == letter|32 {
			return
		}
	}

	// Try this piece at every position on the board
	for y := range 8 {
		for x := range 8 {
			if brd.PlacePiece(piece, x, y) {
				// Track the two biggest pieces as they are placed
				if piece.Name >= 'j' && piece.Name <= 'k' || piece.Name >= 'J' && piece.Name <= 'K' {
					// fmt.Printf("Placed %c at (%d, %d)\n", letter, x, y)
					// brd.Print()
				}
				solve(brd, index+1)
			}
			brd.RemovePiece(piece)
		}
	}
}

func main() {

	brd := gridlock.CreateBoard()

	// brd.PlacePiece(gridlock.GetPieceByName('A'), 5, 5)
	// brd.PlacePiece(gridlock.GetPieceByName('b'), 7, 0)
	// brd.PlacePiece(gridlock.GetPieceByName('C'), 0, 3)

	// brd.PlacePiece(gridlock.Pieces['A'], 0, 0)
	// brd.PlacePiece(gridlock.Pieces['C'], 1, 0)
	// brd.PlacePiece(gridlock.Pieces['B'], 4, 0)
	// brd.PlacePiece(gridlock.Pieces['F'], 6, 0)
	// brd.PlacePiece(gridlock.Pieces['D'], 0, 1)
	// brd.PlacePiece(gridlock.Pieces['g'], 4, 1)
	// brd.PlacePiece(gridlock.Pieces['H'], 0, 2)

	// fmt.Println("Initial board:")
	// brd.Print()
	solve(&brd, 0)

	fmt.Println("Total solutions found: ", total_sols)
}
