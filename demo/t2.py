import pygame
pygame.init()

screen_width, screen_height = 800,600
screen_surface = pygame.display.set_mode((screen_width, screen_height))

sky_surface_raw = pygame.image.load("pics/sky.png")
sky_raw_width, sky_raw_height = sky_surface_raw.get_size()
sky_surface = pygame.transform.scale(sky_surface_raw, (screen_width, sky_raw_height))

grass_surface_raw = pygame.image.load("pics/grass.png")
grass_surface= pygame.transform.scale(grass_surface_raw, (screen_width,screen_height-sky_raw_height))



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  pygame.display.update()
# End while