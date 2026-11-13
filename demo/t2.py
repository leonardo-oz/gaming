from health_bar import Heath_Bar_Heart
from ninja import Ninja
from falling_object import Bomb,Aid,Treasure
from ninja_config import NinjaState
from explosive import Explosive
from score_board import ScoreBoared
from game_event import GameEvent
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

pygame.mixer.music.load("sounds/background_ninja.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)


ninja_width,ninja_height= 80,100
vel=5
clock= pygame.time.Clock()
fps = 60



# Create a Heath Bar 
heart = pygame.image.load("pics/heart.png").convert_alpha()
heart_surface= pygame.transform.scale(heart,(20,20))
h= Heath_Bar_Heart(heart_surface,20,10)

score_board = ScoreBoared(pygame.Rect(screen_width-200,0,200,100))




nj_ini_rec = pygame.Rect(screen_width//2,
                        #  sky_raw_height-ninja_height//2+3,
                        screen_height-ninja_height-10,
                         ninja_width,ninja_height)
ninja = Ninja(nj_ini_rec,vel=vel)
ninja_group = pygame.sprite.GroupSingle(ninja)



pygame.time.set_timer(GameEvent.SPAWN_BOMB_EVENT,2000)
pygame.time.set_timer(GameEvent.SPAWN_AID_EVENT, 5000)
pygame.time.set_timer(GameEvent.SPAWN_TREASURE_EVENT, 3000)



def _create_explosive_surface_list(w,h,num_repeats=1):
  l = []
  for i in range(0,4):
    for j in range(0,num_repeats):
      explosive_surface_raw = pygame.image.load(f"pics/explosive_{i}.png")
      explosive_surface = pygame.transform.scale(explosive_surface_raw,(w,h))
      l.append(explosive_surface)
  return l
# End method


explosive_surface_list = []
explosive_w, explosive_h=100,100
bomb_w, bomb_h = 50,50
aid_w, aid_h = 50,50
t_w , t_h = 50,50


running = True

explosive_group = pygame.sprite.Group()
explosive_frames = _create_explosive_surface_list(explosive_w,explosive_h,3)
falling_objects_group = pygame.sprite.Group()


while running:
  clock.tick(fps)  # Use Clock instead of delay for consistent frame pacing
  # event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        h.update()
        print("1 Key pressed:")
    elif event.type == GameEvent.SPAWN_BOMB_EVENT:
      bomb_rec= pygame.Rect(random.randint(0,screen_width-bomb_w-1),0, bomb_w, bomb_h)
      falling_objects_group.add(Bomb(bomb_rec,vel = random.randint(1,4),acc=random.random()))
      print("Bomb event triggered")
    elif event.type == GameEvent.SPAWN_AID_EVENT:
      aid_rec = pygame.Rect(random.randint(0,screen_width-aid_w-1),0, aid_w, aid_h)
      falling_objects_group.add(Aid(aid_rec, vel = random.randint(1,3), acc=random.random()))
    elif event.type == GameEvent.SPAWN_TREASURE_EVENT:
      treasure_rec = pygame.Rect(random.randint(0,screen_width-t_w-1),0, t_w, t_h)
      falling_objects_group.add(Treasure(treasure_rec, vel = random.randint(1,3), acc=random.random()))
    elif event.type == GameEvent.BOMB_EXPLODED_EVENT:
      explosive_rect = pygame.Rect(event.x,event.y,explosive_w,explosive_h)
      explosive = Explosive(pygame.Rect(event.x,event.y,explosive_w,explosive_h),explosive_frames)
      explosive_group.add(explosive)
    ninja.handle_events(event)

  # End for 


  # hanldle key presses for movement
  ninja_group.update(screen_width)
  explosive_group.update()
  falling_objects_group.update(screen_height)
  
 
  hits = pygame.sprite.spritecollide(ninja, falling_objects_group, dokill = True )
  if ninja.is_alive:
    for hit_object in hits:
      hit_object.apply_effect(ninja)


  screen_surface.blit(sky_surface, (0,0))
  screen_surface.blit(grass_surface, (0,sky_raw_height))
  h.draw(screen_surface,ninja.num_of_lives)
  ninja_group.draw(screen_surface)
  pygame.draw.rect(screen_surface, (255,0,0), ninja.rect, 2)  # Draw a red rectangle around the ninja for debugging
  explosive_group.draw(screen_surface)
  falling_objects_group.draw(screen_surface)
  score_board.draw(screen_surface,ninja.score)

  pygame.display.update()
# End while

pygame.quit()