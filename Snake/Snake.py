import pygame
import math
import random
import tkinter

class snake(object):
	body = []
	turns = {}

	def init(self, color, pos):
		self.color = color
		self.head = cube(pos)
		self.body.append(self.head)
		self.dirnx = 0
		self.dirny = 1

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			keys = pygame.key.get_pressed()

			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dirnx = -1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_RIGHT]:
					self.dirnx = 1
					self.dirny = 0
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				if keys[pygame.K_UP]:
					self.dirnx = 0
					self.dirny = -1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

				elif keys[pygame.K_DOWN]:
					self.dirnx = 0
					self.dirny = 1
					self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

			for i, c in enumerate(self.body):
				p = c.pos[:]
				if p in self.turns[p]:
					turn = self.turns[p]
					c.move(turn[0], turn[1])
					if i == len(self.body) - 1:
						self.turns.pop(p)

	def reset(self):



def drawGrid(w, rows, surface):
	sizeBtwn = w // rows
	x, y = 0, 0

	for i in range(rows):
		x += sizeBtwn
		y += sizeBtwn

		pygame.draw.line(surface, (255,255,255), (x, 0),(x, w))
		pygame.draw.line(surface, (255,255,255), (0, y),(w, y))

def redrawWindow(surface):
	global width, rows
	surface.fill((0,0,0))
	drawGrid(width, rows, surface)
	pygame.display.update()





def main():
	global width, rows
	width = 500
	rows = 20
	win = pygame.display.set_mode((width, width))
	#s = snake((255, 0, 0),(10, 10))
	flag = True
	clock = pygame.time.Clock()

	while flag:
		pygame.time.delay(50)
		clock.tick(10)

		redrawWindow(win)

main()