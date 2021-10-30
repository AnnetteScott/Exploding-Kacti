#Libraries
import pygame
from pygame import image
from threading import Thread
from pygame.constants import MOUSEBUTTONDOWN
pygame.font.init()
pygame.init()
#Function Files
from GAME.Settings import constants
from GAME.Settings import player
from GAME.Settings import cactus_items
from GAME.Engine import functions
from GAME.Engine import routines


#Screen and global variables
SCREEN = constants.SCREEN
MOUSE_POS = pygame.mouse.get_pos()
POND_DIM = 128
SCREEN_CENTER = constants.SCREEN_CENTER
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_WIDTH = constants.SCREEN_WIDTH
pygame.display.set_caption("Exploding Kacti")

#####################################################################################
#-----------------------------------Draws the Game----------------------------------#
#####################################################################################
def draw_backdrop():
	#Draws Background Image
	image_dim = 500
	BACKGROUND = pygame.image.load('GAME/Images/sand_background.png').convert_alpha()
	BACKGROUND = pygame.transform.scale(BACKGROUND, (image_dim, image_dim))
	for y in range(0, SCREEN_HEIGHT, image_dim):
		for x in range(0, SCREEN_WIDTH, image_dim):
			SCREEN.blit(BACKGROUND, (x, y))

	#Draws pond in middle of screen
	POND = pygame.image.load('GAME/Images/ponds/pond10.png')
	POND = pygame.transform.scale(POND, (POND_DIM, POND_DIM))
	pond_offsetX = SCREEN_WIDTH / 2 - POND_DIM / 2
	pond_offsetY = SCREEN_HEIGHT / 2 - POND_DIM / 2
	SCREEN.blit(POND, (pond_offsetX, pond_offsetY))

def draw_water_meter():
	bar_height = 15
	bar_width =  POND_DIM * (player.pond_item['water_amount'] / 100)
	barX = SCREEN_CENTER['x'] - POND_DIM / 2 
	barY = SCREEN_CENTER['y'] + POND_DIM / 2
	barY += bar_height
	pygame.draw.rect(SCREEN, (0, 0, 255), (barX, barY, bar_width, bar_height)) #Red Fill
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, POND_DIM, bar_height), 3) #Outline
	routines.createText('Water', 15, barX + POND_DIM / 2 - 21, barY - 1) #Text
	
def draw_health_meter():
	bar_height = 15
	bar_width = POND_DIM * (player.player['health'] / 100)
	barX = SCREEN_CENTER['x'] - POND_DIM / 2 
	barY = SCREEN_CENTER['y'] + POND_DIM / 2
	pygame.draw.rect(SCREEN, (255, 0, 0), (barX, barY, bar_width, bar_height)) #Red Fill
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, POND_DIM, bar_height), 3) #Outline
	routines.createText('Health', 15, barX + POND_DIM / 2 - 26, barY - 1) #Text

#####################################################################################
#----------------------------------------Cacti--------------------------------------#
#####################################################################################

def draw_cactus(cacti_object):
	cacti_type = cacti_object['cacti_type']
	pos = cacti_object['pos']
	cactus = pygame.image.load('GAME/Images/sprites/'+ cacti_type +'.png').convert_alpha()
	cactus = pygame.transform.scale(cactus, (cactus_items.cacti_dim, cactus_items.cacti_dim))
	SCREEN.blit(cactus, (pos['x'], pos['y']))

def check_cacti_num():
	if len(cactus_items.all_cacti.keys()) < cactus_items.max_num_of_cacti:
		cacti_object = routines.spawnCactus()
		pygame.time.delay(1000)
		draw_cactus(cacti_object)



#####################################################################################
#------------------------------------Click Events-----------------------------------#
#####################################################################################

def click_events():
	if functions.checkObjectClick(POND_DIM, POND_DIM, SCREEN_CENTER['x'], SCREEN_CENTER['y']):
		routines.changeWater(50)
		draw_water_meter()
		pygame.display.update()
		


#PUT EVERYTHING BEFORE THIS
#####################################################################################
#--------------------------------------MAIN GAME------------------------------------#
#####################################################################################
#MAIN GAME
	
run = True
while run:
	pygame.time.delay(50)
	draw_backdrop()
	draw_water_meter()
	draw_health_meter()
	thread1 = Thread(target=check_cacti_num)
	thread2 = Thread(target=routines.moveAllCacti())
	thread1.start()
	#pygame.time.delay(50)
	thread2.start()
	
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:		
			click_events()
			run = False
	
	pygame.display.update()

pygame.quit()


