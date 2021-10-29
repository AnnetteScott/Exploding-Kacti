import math
import random
import pygame

def zeropad(string, length):
	string = str(string)
	pad = ""
	for index in range(length - len(str)):
		pad += "0"
	return pad + string


def getLinearDistance(p1, p2):
  	return math.sqrt(((p2['x'] - p1['x']) * (p2['x'] - p1['x'])) + ((p2['y'] - p1['y']) * (p2['y'] - p1['y'])))


def degToRad(deg):
	return deg * (math.pi / 180)


def radToDeg(rad):
  	return rad * (180 / math.pi)


def between(x, min, max):
	a_bool = x >= min and x <= max
	return a_bool


def checkCollision(obj1, obj2):
	return (obj1['size'] + obj2['size']) <= getLinearDistance(obj1['pos'], obj2['pos'])

#pass width and height of the object and the x and y coordintes of it's center
def checkObjectClick(width, height, x, y):
	MOUSE_POS = pygame.mouse.get_pos()
	if between(MOUSE_POS[0], x - width/2, x + width/2) and between(MOUSE_POS[1], y - height/2, y + height/2):
		return True
	else:
		return False


def generateID():
	char_pool = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	id = ""
	for index in range(10):
		id += char_pool[random.randrange(0, len(char_pool))]
	return id