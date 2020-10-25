import numpy as np
import math
import pygame
import sys
rows = 6
columns = 7
blue = (0, 0, 255)
black = (0, 0, 0)

def drawBoard(board):
	for c in range(columns):
		for r in range(rows):
			pygame.draw.rect(screen, blue, (c * squareSize, r * squareSize + squareSize, squareSize, squareSize))
			pygame.draw.circle(screen, black, (c * squareSize + squareSize // 2, r * squareSize + squareSize + squareSize // 2), radius)

def createBoard():
	board = np.zeros((rows, columns))
	return board

def dropPiece(board, row, col, piece):
	board[row][col] = piece


def isValidLoc(board, col):
	return board[rows - 1, col] == 0

def getNextOpenRow(board, col):
	for r in range(rows):
		if board[r][col] == 0:
			return r

def winningMove(board, piece):
	#horizontal win
	for c in range(columns - 3):
		for r in range(rows):
			if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
				return True

	#Vertical win
	for c in range(columns):
		for r in range(rows - 3):
			if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
				return True

	# positive diagonal win
	for c in range(columns - 3):
		for r in range(rows - 3):
			if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
				return True

	# negative diagonal win
	for c in range(columns - 3, columns):
		for r in range(rows - 3, rows):
			if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
				return True

def printBoard(board):
	print(np.flip(board, 0))

board = createBoard()
turn = 0
squareSize = 100
radius = int(squareSize / 2.15)
width = squareSize * columns
height = squareSize * (rows + 1)

pygame.init()

screen = pygame.display.set_mode((width, height))
drawBoard(board)
pygame.display.update()


while  1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)

		if event.type == pygame.MOUSEBUTTONDOWN:
		
			turn += 1
			turn %= 2 


''' # Player 1
	if turn == 0:
		col = int(input("Player 1:"))
		if isValidLoc(board, col):
			row = getNextOpenRow(board, col)
			dropPiece(board, row, col, 1)
		if winningMove(board, 1):
			print("Player 1 won! Congrats!!!")
			break
		
	# Player 2
	else:
		col = int(input("Player 2:"))
		if isValidLoc(board, col):
			row = getNextOpenRow(board, col)
			dropPiece(board, row, col, 2)
		if winningMove(board, 2):
			print("Player 2 won! Congrats!!!")
			break
	printBoard(board)'''