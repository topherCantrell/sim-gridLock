package gridlock

var TotalCount int
var JustOneSolution Board

func CountSolve(brd *Board, allowed_pieces *[]Piece) (int, Board) {
	TotalCount = 0
	JustOneSolution = CreateBoard()
	countSolutionsRecursive(brd, allowed_pieces)
	return TotalCount, JustOneSolution
}

func countSolutionsRecursive(brd *Board, allowed_pieces *[]Piece) {
	// if TotalCount > 50_000_000 {
	// 	return
	// }
	// Find the largest piece that isn't on the given board
	fnd := -1
	for i, p := range *allowed_pieces {
		if !brd.HasPiece(p.Name) {
			fnd = i
			break
		}
	}
	if fnd < 0 {
		// All pieces are on the board
		TotalCount++
		if TotalCount == 1 {
			JustOneSolution = *brd
		}
		for _, p := range *brd {
			if p == '.' {
				panic("Invalid solution: empty space found")
			}
		}
		return
	}
	piece := (*allowed_pieces)[fnd]

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
					countSolutionsRecursive(brd, allowed_pieces)
				}
				brd.RemovePiece(piece)
			}
		}
	}
}

// Place all remaining pieces on the board. Add any solutions found to the
// given list of solutions.
func Solve(brd *Board, allowed_pieces *[]Piece, retSolutions *[]Board) {

	// Find the largest piece that isn't on the given board
	fnd := -1
	for i, p := range *allowed_pieces {
		if !brd.HasPiece(p.Name) {
			fnd = i
			break
		}
	}
	if fnd < 0 {
		// All pieces are on the board
		*retSolutions = append(*retSolutions, *brd)
		return
	}
	piece := (*allowed_pieces)[fnd]

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
					Solve(brd, allowed_pieces, retSolutions)
				}
				brd.RemovePiece(piece)
			}
		}
	}

}
