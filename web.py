import pygame
pygame.init()
height = 720
width = 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Squarey")
x = 100
y = 100
baddyX = 300
baddyY = 300
vel = 6
baddyVel = 4
run = True

def draw_background():
      image_dim = 500
      BACKGROUND = pygame.image.load('sand_background.png').convert_alpha()
      BACKGROUND = pygame.transform.scale(BACKGROUND, (image_dim, image_dim))
      for y in range(0, height, image_dim):
            for x in range(0, width, image_dim):
                screen.blit(BACKGROUND, (x,y))


def draw_game():
      draw_background()
      pygame.draw.rect(screen, (0, 0, 255), (x, y, 20, 20))
      pygame.draw.rect(screen, (255, 0, 0), (baddyX, baddyY, 40, 40))
      pygame.display.update()


while run:
      pygame.time.delay(100)

      if baddyX < x - 10: 
            baddyX = baddyX + baddyVel 
            draw_game() 
      elif baddyX > x + 10:
          draw_game()
          baddyX = baddyX - baddyVel
      elif baddyY < y - 10: 
            baddyY = baddyY + baddyVel 
      elif baddyY > y + 10:
          baddyY = baddyY - baddyVel
      else:
          run = False
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
            x -= vel

      if keys[pygame.K_RIGHT]:
            x += vel
      
      if keys[pygame.K_UP]:
            y -= vel
      
      if keys[pygame.K_DOWN]:
            y += vel
      
      draw_game()
          
pygame.quit()