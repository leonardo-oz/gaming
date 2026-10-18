from health_bar import Health_Bar
from health_bar import Heath_Bar_Heart
from ninja import Ninja
from bomb import Bomb
import random

import pygame
pygame.init()
pygame.mixer.init()


screen_width, screen_height = 800,600
screen_surface = pygame.display.set_mode((screen_width, screen_height))

sky_surface_raw = pygame.image.load("pics/sky.png")
sky_raw_width, sky_raw_height = sky_surface_raw.get_size()
sky_surface = pygame.transform.scale(sky_surface_raw, (screen_width, sky_raw_height))

grass_surface_raw = pygame.image.load("pics/grass.png")
grass_surface= pygame.transform.scale(grass_surface_raw, (screen_width,screen_height-sky_raw_height))

hit_sound = pygame.mixer.Sound("sounds/cartoon_music-bomb-explosion-large-amp-short-517328.mp3")
pygame.mixer.music.load("sounds/background_ninja.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)
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
SPAWN_BOMB_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(SPAWN_BOMB_EVENT,2000)


def _create_bomb_surface(w,h):
  i = random.randint(1,3)
  bomb_surface_raw = pygame.image.load(f"pics/bomb_{i}.png")
  bomb_surface = pygame.transform.scale(bomb_surface_raw,(w,h))

  return bomb_surface

bomb_w, bomb_h = 50,50
bomb = None
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
    elif event.type == SPAWN_BOMB_EVENT:
      bomb_surface = _create_bomb_surface(bomb_w,bomb_h)

      bomb_rec= pygame.Rect(random.randint(0,screen_width-bomb_w-1),0, bomb_w, bomb_h)
      bomb = Bomb(bomb_rec, bomb_surface,vel = random.randint(5,10) )
      print("Bomb event triggered")
    ninja.handle_events(event)


  # hanldle key presses for movement
  keys = pygame.key.get_pressed()

  
  # Horizontal movement (available in both modes)
  ninja.update(keys, screen_width)
  if bomb and bomb.active:
    bomb.update(screen_height)
    # check if bomb collides with ninja
    if bomb.rec.colliderect(ninja.rec):
    # if yes,
      # decrement a heart from heath bar
      h.update()
      hit_sound.play()
      # set bomb status not active
      bomb.active = False

  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  h.draw(screen_surface)
  # screen_surface.blit(current_ninja_surface, current_ninja_rect)
  ninja.draw(screen_surface)

  if bomb:
    bomb.draw(screen_surface)

  pygame.display.update()
# End while