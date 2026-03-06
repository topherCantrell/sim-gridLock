package main

import (
	"fmt"
	"os"

	"github.com/topherCantrell/sim-gridLock/pkg/gridlock"
)

func main() {

	if len(os.Args) < 2 {
		fmt.Println("Usage: setofpieces set")
		return
	}

	// The character names of the pieces
	pieces := os.Args[1]

	// The set of pieces
	givenPieces := make([]gridlock.Piece, 0)
	for _, c := range pieces {
		givenPieces = append(givenPieces, gridlock.GetExtendedPieceByName(byte(c)))
	}

	// The blank board
	brd := gridlock.CreateBoard()

	// Find all solutions
	total, one := gridlock.CountSolve(&brd, &givenPieces)

	x := ""
	for _, i := range one {
		x += string(i)
	}

	fmt.Println(pieces, total, x)

}
