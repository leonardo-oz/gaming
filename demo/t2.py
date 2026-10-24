from health_bar import Health_Bar
from health_bar import Heath_Bar_Heart
from ninja import Ninja
from falling_object import Falling_Object
from ninja_config import NinjaState
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

bomb_hit_sound = pygame.mixer.Sound("sounds/cartoon_music-bomb-explosion-large-amp-short-517328.mp3")
aid_hit_sound = pygame.mixer.Sound("sounds/heal.mp3")
treasure_hit_sound= pygame.mixer.Sound("sounds/coin.mp3")
pygame.mixer.music.load("sounds/background_ninja.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)


ninja_width,ninja_height= 80,100
vel=5
clock= pygame.time.Clock()




# Create a Heath Bar 
heart = pygame.image.load("pics/heart.png").convert_alpha()
heart_surface= pygame.transform.scale(heart,(20,20))
h= Heath_Bar_Heart(heart_surface,20,10)

# Create a ninja object
nj_file_dic = {
    NinjaState.STANDING: "nj_stand.png",
    NinjaState.RUNNING_RIGHT: "nj_run_right.png",
    NinjaState.RUNNING_LEFT: "nj_run_left.png",
    NinjaState.MEDITATING: "nj_meditaing.png",
    NinjaState.BRUCE_LEE: "nj_brucelee.png",
    NinjaState.DEAD: "nj_dead.png"

  }

nj_ini_rec = pygame.Rect(screen_width//2,
                        #  sky_raw_height-ninja_height//2+3,
                        screen_height-ninja_height-10,
                         ninja_width,ninja_height)
ninja = Ninja(nj_ini_rec,nj_file_dic,vel=vel)
ninja_group = pygame.sprite.GroupSingle(ninja)



SPAWN_BOMB_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BOMB_EVENT,2000)
SPAWN_AID_EVENT = pygame.USEREVENT +2 
pygame.time.set_timer(SPAWN_AID_EVENT, 5000)
SPAWN_TREASURE_EVENT = pygame.USEREVENT +3 
pygame.time.set_timer(SPAWN_TREASURE_EVENT, 3000)
def _create_bomb_surface(w,h):
  i = random.randint(1,3)
  bomb_surface_raw = pygame.image.load(f"pics/bomb_{i}.png")
  bomb_surface = pygame.transform.scale(bomb_surface_raw,(w,h))

  return bomb_surface

def _create_treasure_surface(w,h):
  i = random.randint(1,3)
  treasure_surface_raw = pygame.image.load(f"pics/treasure_{i}.png")
  treasure_surface = pygame.transform.scale(treasure_surface_raw,(w,h))

  return treasure_surface


def _create_aid_surface(w,h):
  aid_surface_raw = pygame.image.load(f"pics/aid.png")
  aid_surface = pygame.transform.scale(aid_surface_raw,(w,h))

  return aid_surface


bomb_w, bomb_h = 50,50
aid_w, aid_h = 50,50
t_w , t_h = 50,50
running = True
bomb_group = pygame.sprite.Group()
aid_group = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()
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
      bomb = Falling_Object(bomb_rec, bomb_surface,vel = random.randint(1,4),acc=random.random())
      bomb_group.add(bomb)
      print("Bomb event triggered")
    elif event.type == SPAWN_AID_EVENT:
      aid_surface = _create_aid_surface(aid_w, aid_h) 
      aid_rec = pygame.Rect(random.randint(0,screen_width-aid_w-1),0, aid_w, aid_h)
      aid = Falling_Object(aid_rec,aid_surface, vel = random.randint(1,3), acc=random.random())
      aid_group.add(aid)
    elif event.type == SPAWN_TREASURE_EVENT:
      treasure_surface = _create_treasure_surface(t_w, t_h) 
      treasure_rec = pygame.Rect(random.randint(0,screen_width-t_w-1),0, t_w, t_h)
      treasure = Falling_Object(treasure_rec,treasure_surface, vel = random.randint(1,3), acc=random.random())
      treasure_group.add(treasure)

    
    ninja.handle_events(event)

  # End for 


  # hanldle key presses for movement
  ninja_group.update(screen_width)
  bomb_group.update(screen_height)
  aid_group.update(screen_height)
  treasure_group.update(screen_height)
  

  bomb_hits = pygame.sprite.spritecollide(ninja, bomb_group, dokill = True )
  if bomb_hits:
    for _ in bomb_hits:
      ninja.update_lives(-1)
      bomb_hit_sound.play()
      if ninja.num_of_lives<=0:
          ninja.ends()
          print(ninja)

  aid_hits = pygame.sprite.spritecollide(ninja, aid_group, dokill = True)
  if aid_hits:
    for _ in aid_hits:
      ninja.update_lives(1)
      aid_hit_sound.play()
  # end if
  treasure_hits = pygame.sprite.spritecollide(ninja, treasure_group, dokill = True)
  if treasure_hits:
    for _ in treasure_hits:
      treasure_hit_sound.play()
  # end if
    


  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  h.draw(screen_surface,ninja.num_of_lives)
  ninja_group.draw(screen_surface)
  bomb_group.draw(screen_surface)
  aid_group.draw(screen_surface)
  treasure_group.draw(screen_surface)

  pygame.display.update()
# End while