import chess

#creates the board
board = chess.Board()

#shows chess board
print(board)

while True:
	board.legal_moves
	#White move
	Whitemove = input("Enter your move in notation form: ")
	board.push_san(Whitemove)
	print(board)

	Blackmove = input("Enter your move: ")
	board.push_san(Blackmove)
	print(board)

	#ENDGAMES
	#checks for check
	check = board.is_check()
	checkmate = board.is_checkmate()
	draw = board.is_stalemate()

	if check:
		print("You are in check!")
	if checkmate:
		print("your opponent checkmated you...")
		break
	if draw:
		print("Everyone won it is a stalemate...")
		break
