
from pygame.event import Event
import pygame
from ninja_config import NinjaState


class Ninja(pygame.sprite.Sprite):
  MAX_LIVES = 5

  def __init__(self,
               ninja_rect: pygame.Rect,
               status_file_dict: dict,
               default_status=NinjaState.STANDING,
               vel: int = 5
               
               ):
    super().__init__()
    self.initial_rec
    self.rect = ninja_rect
    self.status_surface_dict = self._create_status_surface_dic(status_file_dict)
    self.default_status = default_status
    self.current_status = default_status
    self.vel = vel 
    self.num_of_lives = Ninja.MAX_LIVES
    self.score = 0

  # End __init__ method

  
  @property
  def image(self):
    return self.status_surface_dict[self.current_status]

  @property
  def is_alive(self) -> bool:
    return self.num_of_lives > 0 and self.current_status != NinjaState.DEAD

  def _create_status_surface_dic( self, status_file_dict):
    status_dict= {}
    for k in status_file_dict:
      ninja=pygame.image.load(f"pics/{status_file_dict[k]}").convert_alpha()
      ninja_surface=pygame.transform.scale(ninja,(self.rect.width, self.rect.height))
      status_dict[k] = ninja_surface
    # end for key value
    return status_dict


  def __str__(self):
    return f"current status: {self.current_status.name}, \
      position: {self.rect.x},{self.rect.y}, \
      score : {self.score}"
  
  def handle_events(self,event: Event):
    """handle discrete (single-press / release) events."""

    if not self.is_alive:
      return 
    
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

  # End handle_events method

  
  def update(self, screen_width: int):

    if not self.is_alive:
      return 

    # handle continuous event
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
      self.rect.left -= self.vel
      if self.rect.left <= 0:
        self.rect.left = 0
        
      print("Left pressed:", self.rect.left)
            
    if keys[pygame.K_RIGHT]:
      self.rect.right += self.vel
      if self.rect.right>= screen_width:
        self.rect.right = screen_width

  # end update method 


  def update_lives(self,v: int):
    if not self.is_alive and v <0:
      return # dead ninja cannot lose more lives
    
    self.num_of_lives = max(0, self.num_of_lives + v) 
    if self.num_of_lives == 0:
      self.current_status = NinjaState.DEAD

  # End method
    
  def update_score(self,v: int):
    if self.is_alive:
      self.score = max(0,self.score + v)
  # End update_score method

  def reset(self):
    self.current_status = self.default_status
    self.num_of_lives = Ninja.MAX_LIVES
    self.score = 0
  # End reset method

# End Ninja class

