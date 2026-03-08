package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/topherCantrell/sim-gridLock/pkg/gridlock"
)

func main() {

	if len(os.Args) < 2 {
		fmt.Println("Usage: solver inputFile [outputFile]")
		return
	}

	// The challenge input file (see challenge.txt for details)
	inputFile := os.Args[1]

	// Output binary file (or stdout if not provided)
	outputFile := ""
	if len(os.Args) > 2 {
		outputFile = os.Args[2]
	}

	var err error
	var input = []byte{}

	// Read the lines of the input file
	input, err = os.ReadFile(inputFile)
	if err != nil {
		fmt.Println("Error reading input file: ", err)
		return
	}
	lines := strings.Split(string(input), "\n")

	// Create a starting board (and pieces) from the input file

	pos := 0
	width := 0
	data := make([]byte, 0)
	givenPieces := make([]gridlock.Piece, 0)
	for _, line := range lines {
		line = strings.TrimSpace(line)
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}
		if strings.HasPrefix(line, ">") {
			letter := line[1]
			width := int(line[3] - '0')
			height := int(line[5] - '0')
			color := line[7:]
			givenPieces = append(givenPieces, gridlock.Piece{Name: letter, Width: width, Height: height, Color: color})
			continue
		}
		width = len(line)
		for _, c := range line {
			data = append(data, byte(c))
			pos += 1
		}
	}

	brd := gridlock.CreateBoard(width, len(data)/width)
	copy(brd.Cells, data)

	// Find all solutions from the given starting point
	fmt.Println("Solving Board:")
	brd.Print()
	solutions := make([]gridlock.Board, 0)
	if len(givenPieces) > 0 {
		fmt.Println("Given pieces: ")
		for _, piece := range givenPieces {
			fmt.Printf("%c: %dx%d %s\n", piece.Name, piece.Width, piece.Height, piece.Color)
		}
		gridlock.Solve(&brd, &givenPieces, &solutions)
	} else {
		gridlock.Solve(&brd, &gridlock.Pieces, &solutions)
	}

	// Create the output file if it was provided
	var file *os.File = nil
	if outputFile == "" {
		for _, solution := range solutions {
			fmt.Println("Solution:")
			solution.Print()
		}
	} else {
		file, err = os.Create(outputFile)
		if err != nil {
			fmt.Println("Error creating output file: ", err)
			return
		}
		defer file.Close()
		for _, solution := range solutions {
			_, err = file.Write(solution.Cells)
			if err != nil {
				fmt.Println("Error writing to output file: ", err)
				return
			}
		}
	}

	fmt.Println("Total solutions found: ", len(solutions))

}
