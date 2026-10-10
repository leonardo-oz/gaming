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
ninja_standing_trsfm= pygame.transform.scale(ninja_standing,(ninja_width,ninja_height))
ninja_standing_rect= ninja_standing_trsfm.get_rect(center=(screen_width//2, sky_raw_height-ninja_height//2+3))

vel=5
clock= pygame.time.Clock()

running = True
while running:
  clock.tick(60)  # Use Clock instead of delay for consistent frame pacing
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # end for loop

  keys = pygame.key.get_pressed()

  # Horizontal movement (available in both modes)
  if keys[pygame.K_LEFT]:
    ninja_standing_rect.left -= vel
    if ninja_standing_rect.left <= 0:
      ninja_standing_rect.left = 0
  if keys[pygame.K_RIGHT]:
    ninja_standing_rect.right += vel
    if ninja_standing_rect.right>= screen_width:
      ninja_standing_rect.right = screen_width
  print(ninja_standing_rect.left, ninja_standing_rect.right)

  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  screen_surface.blit(ninja_standing_trsfm, ninja_standing_rect)
  pygame.display.update()
# End while