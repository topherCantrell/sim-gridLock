package gridlock

type Piece struct {
	Name   byte
	Width  int
	Height int
	Color  string
}

var Pieces = []Piece{
	{'K', 4, 3, "white"},
	{'k', 3, 4, "white"},
	{'J', 3, 3, "white"},
	{'I', 5, 2, "white"},
	{'i', 2, 5, "white"},
	{'H', 4, 2, "white"},
	{'h', 2, 4, "white"},
	{'G', 3, 2, "white"},
	{'g', 2, 3, "white"},
	{'F', 2, 2, "white"},
	{'E', 5, 1, "white"},
	{'e', 1, 5, "white"},
	{'D', 4, 1, "white"},
	{'d', 1, 4, "white"},
	{'C', 3, 1, "white"},
	{'c', 1, 3, "white"},
	{'B', 2, 1, "white"},
	{'b', 1, 2, "white"},
	{'A', 1, 1, "white"},
}

func GetPieceByName(name byte) Piece {
	for _, piece := range Pieces {
		if piece.Name == name {
			return piece
		}
	}
	return Piece{}
}
