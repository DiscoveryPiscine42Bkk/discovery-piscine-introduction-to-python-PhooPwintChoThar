def checkmate(board):
    checkBoard = board.strip().split('\n')
    size = len(checkBoard)

    for row in checkBoard:
        if len(row) != size:
            print("The checkboard is not a square!")
            return

    king = None
    for row in range(size):
        for col in range(size):
            if checkBoard[row][col] == 'K':
                king = (row, col)
                break

    if king is None:
        print("Invalid Checkboard! There is no King.")
        return

    for row in range(size):
        for col in range(size):
            piece = checkBoard[row][col]
            if piece == 'P' and pawnCaptures((row, col), king):
                print("Pawn captured the king. Success!")
                return
            elif piece == 'R' and rookCaptures((row, col), king, checkBoard):
                print("Rook captured the king. Success!")
                return
            elif piece == 'B' and bishopCaptures((row, col), king, checkBoard):
                print("Bishop captured the king. Success!")
                return
            elif piece == 'Q' and queenCaptures((row, col), king, checkBoard):
                print("Queen captured the king. Success!")
                return
            elif piece == '.':
                continue
            elif piece == 'K':
                continue
            else:
                print(f"{piece} is not used to refer to any piece. So it is an empty square.")
                return

    print("No enemy piece can capture the King. Fail!")

def pawnCaptures(pawn, king):
    pRow, pCol = pawn
    return (pRow + 1, pCol - 1) == king or (pRow + 1, pCol + 1) == king

def rookCaptures(rook, king, board):
    boardSize = len(board)
    rRow, rCol = rook
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nRow, nCol = rRow + dr, rCol + dc
        while 0 <= nRow < boardSize and 0 <= nCol < boardSize:
            if board[nRow][nCol] != '.':
                if (nRow, nCol) == king:
                    return True
                break
            if (nRow, nCol) == king:
                return True
            nRow += dr
            nCol += dc
    return False

def bishopCaptures(bishop, king, board):
    size = len(board)
    row, col = bishop
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < size and 0 <= c < size:
            if board[r][c] != '.':
                if (r, c) == king:
                    return True
                break
            if (r, c) == king:
                return True
            r += dr
            c += dc
    return False

def queenCaptures(queen, king, board):
    return rookCaptures(queen, king, board) or bishopCaptures(queen, king, board)
