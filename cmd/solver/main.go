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

	// Create a starting board from the input file
	brd := gridlock.CreateBoard()
	pos := 0
	for _, line := range lines {
		line = strings.TrimSpace(line)
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}
		for _, c := range line {
			brd[pos] = byte(c)
			pos += 1
		}
	}

	// Create the output file if it was provided
	var file *os.File = nil
	if outputFile != "" {
		file, err = os.Create(outputFile)
		if err != nil {
			fmt.Println("Error creating output file: ", err)
			return
		}
		defer file.Close()
	}

	// Find all solutions from the given starting point
	fmt.Println("Solving Board:")
	brd.Print()
	total := gridlock.Solve(&brd, file)
	fmt.Println("Total solutions found: ", total)

}
