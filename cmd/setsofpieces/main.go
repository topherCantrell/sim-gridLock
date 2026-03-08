package main

import (
	"fmt"
	"os"
	"strconv"

	"github.com/topherCantrell/sim-gridLock/pkg/gridlock"
)

func main() {

	if len(os.Args) < 4 {
		fmt.Println("Usage: setofpieces width height pieces")
		return
	}

	width, _ := strconv.Atoi(os.Args[1])
	height, _ := strconv.Atoi(os.Args[2])

	// The character names of the pieces
	pieces := os.Args[3]

	// The set of pieces
	givenPieces := make([]gridlock.Piece, 0)
	for _, c := range pieces {
		givenPieces = append(givenPieces, gridlock.GetExtendedPieceByName(byte(c)))
	}

	// The blank board
	brd := gridlock.CreateBoard(width, height)

	// Find all solutions
	total, one := gridlock.CountSolve(&brd, &givenPieces)

	x := ""
	for _, i := range one.Cells {
		x += string(i)
	}

	fmt.Println(pieces, total, x)

}
