import pygame
import math
import random
from ..Settings import constants
from ..Settings import cactus_items
from ..Engine import functions

def createText(text, font_size, x, y):
	myfont = pygame.font.SysFont('Courier New', font_size)
	textsurface = myfont.render(text, False, (0, 0, 0))
	constants.SCREEN.blit(textsurface,(x,y))

def spawnCactus(type = "normal_cactus"):
	if len(cactus_items.all_cacti.keys()) < cactus_items.max_num_of_cacti:
		pos = {'x': constants.SCREEN_CENTER['x'], 'y': constants.SCREEN_CENTER['y']}
		while functions.getLinearDistance(pos, constants.SCREEN_CENTER) < cactus_items.cacti_min_spawn_distance or functions.between(pos.x, (constants.SCREEN_CENTER['x'] - 75), (constants.SCREEN_CENTER['x'] + 75)):
			pos = {'x': random.randrange(0, constants.SCREEN_WIDTH), 'y': random.randrange(0, constants.SCREEN_HEIGHT)}

		id = functions.generateID()
		new_cactus_object = {
			'id': id,
			'type': type,
			'pos': pos,
			'total_health': cactus_items.cacti_types[type]['health'],
			'remaining_health': cactus_items.cacti_types[type]['health']
		}

		cactus_items.all_cacti[id] = new_cactus_object