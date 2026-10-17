
from pygame.event import Event
import pygame

class Ninja:
  def __init__(self,
               ninja_rect,
               status_file_dict,
               default_status="standing",
               vel = 5):
    self.rec = ninja_rect
    self.status_surface_dict = self._create_status_surface_dic(status_file_dict)
    self.current_status = default_status
    self.vel = vel 

  def _create_status_surface_dic( self, status_file_dict):
    status_dict= {}
    for k in status_file_dict:
      ninja=pygame.image.load(f"pics/{status_file_dict[k]}").convert_alpha()
      ninja_surface=pygame.transform.scale(ninja,(self.rec.width, self.rec.height))
      status_dict[k] = ninja_surface
    # end for key value
    return status_dict


   


  def __str__(self):
    return f"current status: {self.current_status}, position: {self.rec.x},{self.rec.y}, current speed: {self.vel}"
    


  def handle_events(self,event: Event):
    # if event.type == pygame.KEYDOWN:
    #   if event.key == pygame.K_LEFT:
    #     self.current_surface= self.status_surface_dict["run_left.png"]
    #     print("Left Key Down pressed:", event.key)
    #   elif event.key == pygame.K_RIGHT:
    #     self.current_surface= self.status_surface_dict["run_right.png"]
    #     print("Right Key Down pressed:", event.key)
    #   elif event.key == pygame.K_DOWN:
    #       self.current_surface= self.status_surface_dict["meditaing"]
    #       print("Down Key pressed:", event.key)



    #   if event.type == pygame.KEYUP:
    #   print("Key Up pressed:", event.key)
    #   self.current_surface= ninja_standing_surface


    # if event.type == pygame.MOUSEBUTTONDOWN:
    #   print("Mouse Button Down pressed:", event.button)
    #   if self.current_surface.collidepoint(event.pos):
    #     self.current_surface= ninja_brucelee_surface


    # if event.type == pygame.MOUSEBUTTONUP:
    #   print("Mouse Button Up pressed:", event.button)
    #   self.current_surface= ninja_standing_surface

    # Handle non-continuous event
    pass
    
  def update(self,event: Event, screen_width: int):
    # vel=5
    # # handle continuous event
    # if event[pygame.K_LEFT]:
    #         self.rec.left -= vel
    #         if self.rec.left <= 0:
    #           self.rec.left = 0
        
    #         print("Left pressed:", self.rec.left)
            
    # if event[pygame.K_RIGHT]:
    #   self.rec.right += vel
    #   if self.rec.right>= screen_width:
    #     self.rec.right = screen_width

    #   print("Right pressed:", self.rec.right)
    pass

  def draw(self,canva):
    canva.blit(self.status_surface_dict[self.current_status], self.rec)
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