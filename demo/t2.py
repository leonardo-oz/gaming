from health_bar import Health_Bar
from health_bar import Heath_Bar_Heart
from ninja import Ninja

import pygame
pygame.init()

screen_width, screen_height = 800,600
screen_surface = pygame.display.set_mode((screen_width, screen_height))

sky_surface_raw = pygame.image.load("pics/sky.png")
sky_raw_width, sky_raw_height = sky_surface_raw.get_size()
sky_surface = pygame.transform.scale(sky_surface_raw, (screen_width, sky_raw_height))

grass_surface_raw = pygame.image.load("pics/grass.png")
grass_surface= pygame.transform.scale(grass_surface_raw, (screen_width,screen_height-sky_raw_height))


ninja_width,ninja_height= 80,100




vel=5
clock= pygame.time.Clock()




# Create a Heath Bar 
heart = pygame.image.load("pics/heart.jpeg")
heart_surface= pygame.transform.scale(heart,(20,20))
h= Heath_Bar_Heart(heart_surface,5,20,10)

# Create a ninja object
nj_file_dic = {
    "standing": "nj_stand.png",
    "running_right": "nj_run_right.png",
    "running_left": "nj_run_left.png",
    "meditating": "nj_meditaing.png",
    "bruce_lee": "nj_brucelee.png"

  }

nj_ini_rec = pygame.Rect(screen_width//2,sky_raw_height-ninja_height//2+3,ninja_width,ninja_height)
ninja = Ninja(nj_ini_rec,nj_file_dic,vel=vel)

running = True
while running:
  clock.tick(60)  # Use Clock instead of delay for consistent frame pacing
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        h.update()
        print("1 Key pressed:")

    ninja.handle_events(event)


  # hanldle key presses for movement
  keys = pygame.key.get_pressed()

  
  # Horizontal movement (available in both modes)
  ninja.update(keys, screen_width)


  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  h.draw(screen_surface)
  # screen_surface.blit(current_ninja_surface, current_ninja_rect)
  ninja.draw(screen_surface)

  pygame.display.update()
# End while