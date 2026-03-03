package gridlock

type Piece struct {
	Name   byte
	Width  int
	Height int
	Color  string
}

var Pieces = []Piece{
	{'K', 4, 3, "yellow"},
	{'J', 3, 3, "orange"},
	{'I', 5, 2, "blue"},
	{'H', 4, 2, "blue"},
	{'G', 3, 2, "blue"},
	{'F', 2, 2, "red"},
	{'E', 5, 1, "green"},
	{'D', 4, 1, "green"},
	{'C', 3, 1, "white"},
	{'B', 2, 1, "white"},
	{'A', 1, 1, "white"},
}

// Get a piece by its name (upper or lower case).
func GetPieceByName(name byte) Piece {
	name = name & (255 - 32) // Force upper case
	for _, piece := range Pieces {
		if piece.Name == name {
			return piece
		}
	}
	return Piece{}
}
