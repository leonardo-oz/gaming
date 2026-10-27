
from pygame.event import Event
import pygame
from ninja_config import NinjaState


class Ninja(pygame.sprite.Sprite):
  MAX_LIVES = 5

  def __init__(self,
               ninja_rect,
               status_file_dict,
               default_status=NinjaState.STANDING,
               vel = 5
               
               ):
    super().__init__()
    self.rect = ninja_rect
    self.status_surface_dict = self._create_status_surface_dic(status_file_dict)
    self.current_status = default_status
    self.vel = vel 
    self.num_of_lives = Ninja.MAX_LIVES

  
  @property
  def image(self):
    return self.status_surface_dict[self.current_status]

  def _create_status_surface_dic( self, status_file_dict):
    status_dict= {}
    for k in status_file_dict:
      ninja=pygame.image.load(f"pics/{status_file_dict[k]}").convert_alpha()
      ninja_surface=pygame.transform.scale(ninja,(self.rect.width, self.rect.height))
      status_dict[k] = ninja_surface
    # end for key value
    return status_dict


   


  def __str__(self):
    return f"current status: {self.current_status}, position: {self.rect.x},{self.rect.y}, current speed: {self.vel}"
    


  def handle_events(self,event: Event):
    """handle discrete (single-press / release) events."""

    if self.current_status == NinjaState.DEAD:
      return 

    if self.current_status != NinjaState.DEAD:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          self.current_status= NinjaState.RUNNING_LEFT
          print("Left Key Down pressed:", event.key)
        elif event.key == pygame.K_RIGHT:
          self.current_status= NinjaState.RUNNING_RIGHT
          print("Right Key Down pressed:", event.key)
        elif event.key == pygame.K_DOWN:
          self.current_status= NinjaState.MEDITATING
          print("Down Key pressed:", event.key)
      # End if event.type == pygame.KEYDOWN:
       
      elif event.type == pygame.KEYUP:
        print("Key Up pressed:", event.key)
        if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
          self.current_status= NinjaState.STANDING

      elif event.type == pygame.MOUSEBUTTONDOWN:
        print("Mouse Button Down pressed:", event.button)
        if self.rect.collidepoint(event.pos):
          self.current_status= NinjaState.BRUCE_LEE

      elif event.type == pygame.MOUSEBUTTONUP:
        print("Mouse Button Up pressed:", event.button)
        if self.current_status == NinjaState.BRUCE_LEE:
          self.current_status= NinjaState.STANDING
    # End if self.current_status != NinjaState.DEAD:

    # End method

  def ends(self):
    self.current_status = NinjaState.DEAD

     
  
  def update(self, screen_width: int):
    # handle continuous event
    keys = pygame.key.get_pressed()

    if self.current_status == NinjaState.DEAD:
      return 
    if keys[pygame.K_LEFT]:
      self.rect.left -= self.vel
      if self.rect.left <= 0:
        self.rect.left = 0
        
      print("Left pressed:", self.rect.left)
            
    if keys[pygame.K_RIGHT]:
      self.rect.right += self.vel
      if self.rect.right>= screen_width:
        self.rect.right = screen_width

      print("Right pressed:", self.rect.right)
  # end method update


  def update_lives(self,v):
    if self.num_of_lives + v <= Ninja.MAX_LIVES:
      self.num_of_lives = max(0, self.num_of_lives + v) 
    

if __name__ == "__main__":
  pygame.init()
  screen  = pygame.display.set_mode((800,600))
  nj_file_dic = {
    "standing": "nj_stand.png",
    "running_right": "nj_run_right.png",
    "running_left": "nj_run_left.png",
    "meditaiting": "nj_meditaing.png",
    "bruce_lee": "nj_brucelee.png"

  }

  nj_ini_rec = pygame.Rect(10,10,80,100)

  ninja = Ninja(nj_ini_rec,nj_file_dic)
  

  for k in ninja.status_surface_dict:
    print(f"{k}: {ninja.status_surface_dict[k]}")
  # End fopr

  pass