import pygame
pygame.init()

screen_width, screen_height = 800,600
screen_surface = pygame.display.set_mode((screen_width, screen_height))

sky_surface_raw = pygame.image.load("pics/sky.png")
sky_raw_width, sky_raw_height = sky_surface_raw.get_size()
sky_surface = pygame.transform.scale(sky_surface_raw, (screen_width, sky_raw_height))

grass_surface_raw = pygame.image.load("pics/grass.png")
grass_surface= pygame.transform.scale(grass_surface_raw, (screen_width,screen_height-sky_raw_height))
ninja_standing= pygame.image.load("pics/nj_stand.png").convert_alpha()

ninja_width,ninja_height= 80,100
ninja_standing= pygame.transform.scale(ninja_standing,(ninja_width,ninja_height))


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  screen_surface.blit(ninja_standing, (screen_width//2 - ninja_width//2, sky_raw_height-ninja_height+3))
  pygame.display.update()
# End while