
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

    # 1. Meditate: Only K_DOWN triggers and cancels it
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
      self.current_status= NinjaState.MEDITATING

      
    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        if self.current_status == NinjaState.MEDITATING:
          self.current_status= NinjaState.STANDING

    # 2. Bruce Lee Pose: Only Left Mouse Click (button == 1) on sprite
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if self.rect.collidepoint(event.pos):
        self.current_status= NinjaState.BRUCE_LEE

    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
      if self.current_status == NinjaState.BRUCE_LEE:
        self.current_status= NinjaState.STANDING

  # End handle_events method

  
  def update(self, screen_width: int):
    """Handles movement and keeps running animations perfectly synced every frame."""
    if not self.is_alive:
      return 

    # Do not allow movement keys to override special postures
    if self.current_status in (NinjaState.MEDITATING, NinjaState.BRUCE_LEE):
            return

    # handle continuous event
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
      self.rect.left = max(0, self.rect.left - self.vel)
      self.current_status = NinjaState.RUNNING_LEFT
                    
    elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
      self.rect.right = min(screen_width, self.rect.right + self.vel)
      self.current_status = NinjaState.RUNNING_RIGHT
    else:
      self.current_status = NinjaState.STANDING

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

