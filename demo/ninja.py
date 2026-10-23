
from pygame.event import Event
import pygame

class Ninja(pygame.sprite.Sprite):
  def __init__(self,
               ninja_rect,
               status_file_dict,
               default_status="standing",
               vel = 5
               
               ):
    super().__init__()
    self.rect = ninja_rect
    self.status_surface_dict = self._create_status_surface_dic(status_file_dict)
    self.current_status = default_status
    self.vel = vel 

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
    return f"current status: {self.current_status}, position: {self.rec.x},{self.rec.y}, current speed: {self.vel}"
    


  def handle_events(self,event: Event):
    """handle discrete (single-press / release) events."""


    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        self.current_status= "running_left"
        print("Left Key Down pressed:", event.key)
      elif event.key == pygame.K_RIGHT:
        self.current_status= "running_right"
        print("Right Key Down pressed:", event.key)
      elif event.key == pygame.K_DOWN:
        self.current_status= "meditating"
        print("Down Key pressed:", event.key)
      
      



    elif event.type == pygame.KEYUP:
      print("Key Up pressed:", event.key)
      if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN):
        self.current_status= "standing"


    elif event.type == pygame.MOUSEBUTTONDOWN:
      print("Mouse Button Down pressed:", event.button)
      if self.rec.collidepoint(event.pos):
        self.current_status= "bruce_lee"


    elif event.type == pygame.MOUSEBUTTONUP:
      print("Mouse Button Up pressed:", event.button)
      if self.current_status == "bruce_lee":
        self.current_status= "standing"


    # End method

    
  def update(self, screen_width: int):
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

      print("Right pressed:", self.rect.right)
    

  def draw(self,canva):
    canva.blit(self.status_surface_dict[self.current_status], self.rect)
  # End draw method


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