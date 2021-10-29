import pygame
from pygame import image
pygame.init()

#Screen
height = 720
width = 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Exploding Kacti")

#Draws Background Image
def draw_background():
	image_dim = 500
	BACKGROUND = pygame.image.load('Images/sand_background.png').convert_alpha()
	BACKGROUND = pygame.transform.scale(BACKGROUND, (image_dim, image_dim))
	for y in range(0, height, image_dim):
		for x in range(0, width, image_dim):
			screen.blit(BACKGROUND, (x, y))

def draw_pond():
	image_dim = 128
	POND = pygame.image.load('Images/ponds/pond10.png')
	POND = pygame.transform.scale(POND, (image_dim, image_dim))
	offsetX = width / 2 - image_dim / 2
	offsetY = height / 2 - image_dim / 2
	screen.blit(POND, (offsetX, offsetY))



def draw_cactus():
	image_dim = 64
	cactus = pygame.image.load('Images/sprites/normal_cacti.png').convert_alpha()
	cactus = pygame.transform.scale(cactus, (image_dim, image_dim))
	screen.blit(cactus, (150, 150))


def draw_game():
	draw_background()
	draw_pond()
	draw_cactus()

	pygame.display.update()

def main():
	run = True
	while run:
		draw_game()
		pygame.time.delay(10000)
		run = False


main()