def createText(text, font_size, x, y):
	myfont = pygame.font.SysFont('Courier New', font_size)
	textsurface = myfont.render(text, False, (0, 0, 0))
	SCREEN.blit(textsurface,(x,y))