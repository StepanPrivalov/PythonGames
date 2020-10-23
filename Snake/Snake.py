import pygame

def drawGrid(w, rows, surface):
	sizeBtwn = w // rows
	x, y = 0, 0

	for i in range(rows):
		x += sizeBtwn
		y += sizeBtwn

		pygame.draw.line()

def redrawWindow(surface):
	global width, rows
	win.fill((0,0,0))
	drawGrid(width, rows, surface)
	pygame.display.update()





def main():
	global width, rows
	width = 500
	rows = 20
	win = pygame.display.set_mode(width, width)
	s = snake((255, 0, 0),(10, 10))
	flag = True
	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)

		redrawWindow(win)