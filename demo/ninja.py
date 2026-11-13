
from pygame.event import Event
import pygame
from ninja_config import NinjaState
import numpy as np


class Ninja(pygame.sprite.Sprite):
  MAX_LIVES = 5
  status_surface_dict = None
  jumping_frames = None

  def __init__(self,
               ninja_rect: pygame.Rect,
               default_status=NinjaState.STANDING,
               vel_x = 5,
               vel_y_ini = -20
               
               ):
    super().__init__()
    self.rect = ninja_rect
    if not Ninja.status_surface_dict:
      Ninja.setup(*ninja_rect.size)

    if not Ninja.jumping_frames:
      # setp jumping frames
      Ninja.setup_jump(*ninja_rect.size)
      Ninja.status_surface_dict[NinjaState.JUMPING] = Ninja.jumping_frames[2]



    self.current_status = default_status
    self.vel_x = vel_x
    self.vel_y_ini = vel_y_ini 
    self.vel_y  = 0
    self.original_y = self.rect.top
    self.gravity = 2
    self.num_of_lives = Ninja.MAX_LIVES
    self._score = 0


  
  @property
  def image(self):
    return Ninja.status_surface_dict[self.current_status]
  
  
  @property
  def is_alive(self):
      return self.num_of_lives > 0
    # end if
  # end method

  @property
  def score(self) ->int:
    return self._score
  # end method score


  @classmethod
  def setup_jump(cls,nj_w,nj_h):
    cls.jumping_frames = [ pygame.transform.scale(pygame.image.load(f"pics/ninja_jump_{i}.png").convert_alpha(),(nj_w, nj_h))
                        for i in range(6)]
  # end method setup_jump


  @classmethod
  def setup(cls,nj_width, nj_height):
    # Create a ninja object
    nj_file_dic = {
        NinjaState.STANDING: "nj_stand.png",
        NinjaState.RUNNING_RIGHT: "nj_run_right.png",
        NinjaState.RUNNING_LEFT: "nj_run_left.png",
        NinjaState.MEDITATING: "nj_meditaing.png",
        NinjaState.BRUCE_LEE: "nj_brucelee.png",
        NinjaState.DEAD: "nj_dead.png",
        NinjaState.DUCKING: "ninja_duck.png", 
       }
    cls.status_surface_dict = cls._create_status_surface_dic(nj_file_dic,nj_width, nj_height)
  # End setup



  @classmethod
  def _create_status_surface_dic(cls, status_file_dict,nj_w,nj_h):
    status_dict= {}
    for k in status_file_dict:
      ninja=pygame.image.load(f"pics/{status_file_dict[k]}").convert_alpha()
      if k == NinjaState.DEAD:
        ninja_surface=pygame.transform.scale(ninja,(nj_h, nj_w))
      elif k == NinjaState.DUCKING:
        ninja_surface=pygame.transform.scale(ninja,(nj_w, nj_w))
      else:
        ninja_surface=pygame.transform.scale(ninja,(nj_w, nj_h))
      status_dict[k] = ninja_surface
    # end for key value

  
    return status_dict


   


  def __str__(self):
    return f"current status: {self.current_status}, position: {self.rect.x},{self.rect.y}, current speed: {self.vel}, number of lives: {self.num_of_lives}"
    


  def handle_events(self,event: Event):
    """handle discrete (single-press / release) events."""

    if not self.is_alive:
      return 
       
    if event.type == pygame.KEYUP:
      print("Key Up pressed:", event.key)
      if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
        self.current_status= NinjaState.STANDING
    
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        self.current_status= NinjaState.DUCKING
        print("Down Key pressed:", event.key)
      elif event.key == pygame.K_UP:
        self.vel_y = self.vel_y_ini
        self.current_status = NinjaState.JUMPING
        print("Jumping")

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

     
  
  def update(self,screen_height, screen_width: int):
    self.rect = self.image.get_rect(midbottom=self.rect.midbottom)  # Update the rect to match the current image size
    if not self.is_alive:
         return 

    if self.current_status == NinjaState.JUMPING:
      self.vel_y += self.gravity
      # self.ret.y + self.vel_y >= self.original_y:
      self.rect.y = np.clip(self.rect.y+self.vel_y,0,self.original_y)
      if self.rect.y == self.original_y:
        self.current_status = NinjaState.STANDING
        return

     


    if self.current_status in (NinjaState.DUCKING, NinjaState.BRUCE_LEE, NinjaState.JUMPING):
          return

    
    # handle continuous event
    keys = pygame.key.get_pressed()
      
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
      self.current_status= NinjaState.RUNNING_LEFT
      self.rect.left = max(0, self.rect.left - self.vel_x)
      print("Left pressed:", self.rect.left)
            
    if keys[pygame.K_RIGHT]and not keys[pygame.K_LEFT]:
      self.current_status = NinjaState.RUNNING_RIGHT
      self.rect.right = min(screen_width,self.rect.right + self.vel_x)
      print("Right pressed:", self.rect.right)
  # end method update


  def update_lives(self,v):
    if self.is_alive:
      self.num_of_lives = np.clip(self.num_of_lives+v,0,Ninja.MAX_LIVES)
      if self.num_of_lives == 0:
        self.current_status = NinjaState.DEAD
      # end if self.num_of_lives ==0

    # end if self.is_alive:
  # end update_lives method


  def update_score(self, v):
    if self.is_alive:
      self._score+=v
    else:
      return

    # end if not self.is_alive
  # end method update score


      
      
    

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

  ninja = Ninja(nj_ini_rec)
  

  for k in ninja.status_surface_dict:
    print(f"{k}: {ninja.status_surface_dict[k]}")
  # End fopr

  pass