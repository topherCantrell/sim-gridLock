package gridlock

type Piece struct {
	Name   byte
	Width  int
	Height int
	Color  string
}

var OtherPieces = []Piece{
	{'9', 8, 8, "teal"},
	{'8', 8, 7, "coral"},
	{'7', 7, 7, "coral"},
	{'6', 8, 6, "magenta"},
	{'5', 7, 6, "magenta"},
	{'4', 6, 6, "magenta"},
	{'3', 8, 5, "brown"},
	{'2', 7, 5, "brown"},
	{'1', 6, 5, "brown"},
	{'0', 5, 5, "brown"},
	{'Z', 8, 4, "pink"},
	{'Y', 7, 4, "pink"},
	{'X', 6, 4, "pink"},
	{'W', 5, 4, "pink"},
	{'V', 4, 4, "pink"},
	{'U', 8, 3, "gold"},
	{'T', 7, 3, "gold"},
	{'S', 6, 3, "gold"},
	{'R', 5, 3, "gold"},
	{'Q', 8, 2, "purple"},
	{'P', 7, 2, "purple"},
	{'O', 6, 2, "purple"},
	{'N', 8, 1, "cyan"},
	{'M', 7, 1, "cyan"},
	{'L', 6, 1, "cyan"},
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
	for _, piece := range Pieces {
		if piece.Name == name {
			return piece
		}
	}
	return Piece{}
}

func GetExtendedPieceByName(name byte) Piece {
	for _, piece := range Pieces {
		if piece.Name == name {
			return piece
		}
	}
	for _, piece := range OtherPieces {
		if piece.Name == name {
			return piece
		}
	}
	return Piece{}
}
