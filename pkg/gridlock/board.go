package gridlock

import "fmt"

type Board [64]byte

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

func (b *Board) PlacePiece(p Piece, x int, y int) bool {
	for j := 0; j < p.Height; j++ {
		if (y + j) >= 8 {
			return false
		}
		for i := 0; i < p.Width; i++ {
			if (x + i) >= 8 {
				return false
			}
			pos := (y+j)*8 + (x + i)
			if b[pos] != '.' {
				return false
			}
			b[pos] = p.Name
		}
	}
	return true
}

func (b *Board) RemovePiece(p Piece) {
	for index, c := range b {
		if c == p.Name {
			b[index] = '.'
		}
	}
}

func (b *Board) Print() {
	for index, c := range b {
		fmt.Print(string(c))
		if (index+1)%8 == 0 {
			fmt.Println()
		}
	}
}
