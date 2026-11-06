import pygame
from abc import ABC, abstractmethod
from ninja import Ninja
import random



class Falling_Object(pygame.sprite.Sprite,ABC):

   def __init__(self,rec: pygame.Rect, surf: pygame.Surface, vel: float ,acc: float):
      super().__init__()
      self.rect = rec
      self.image = surf
      self.vel = vel
      self.acc = acc

    

   def __str__(self):
    return f"position at {self.rect.x},{self.rect.y}, moving speed: {self.vel}"


   def update(self, screen_height):
      self.rect.y += self.vel
      self.vel += self.acc
      if self.rect.y >= screen_height:

         self.kill()
      # end if
   # end method update

   @abstractmethod
   def apply_efffect(n: Ninja):
     pass



# End Falling_Object Class



class Bomb(Falling_Object):
   sound = None
   surface_list = None
  
   
   def __init__(self, rec:pygame.Rect,vel, acc):

      if not Bomb.sound:
         Bomb.setup_sound()
      # end if not Bomb.s

      if not Bomb.surface_list:
         Bomb.setup_surfaces(*rec.size)

      # random select a surf from surface_list
      i = random.randint(1,3)
      super().__init__(rec, Bomb.surface_list[i], vel, acc)

   @classmethod
   def setup_surfaces(cls,bomb_w, bomb_h):
      cls.surface_list = [pygame.transform.scale(pygame.image.\
                     load(f"pics/bomb_{i}.png"),(bomb_w,\
                                                 bomb_h)) \
                     for i in range(1,4)
      ]
   # End setup_surfaces

   @classmethod
   def setup_sound(cls):
      cls.sound = pygame.mixer.Sound("sounds/cartoon_music-bomb-explosion-large-amp-short-517328.mp3")

   # end setup method

   def apply_efffect(n:Ninja):
      n.update_lives(-1)
      Bomb.sound.play()
   # end apply effect method
# end class Bomb





class Aid(Falling_Object):
   sound = None
   surface_list = None
  
   
   def __init__(self, rec:pygame.Rect,vel, acc):

      if not Aid.sound:
         Aid.setup_sound()
      # end if not Bomb.s

      if not Aid.surface_list:
         Aid.setup_surfaces(*rec.size)

      # random select a surf from surface_list
      super().__init__(rec,random.choice(Aid.surface_list), vel, acc)

   @classmethod
   def setup_surfaces(cls,aid_w, aid_h):
      surface = pygame.transform.scale(pygame.image.\
                     load(f"pics/aid.png"),(aid_w,\
                                                 aid_h)) 
      cls.surface_list.append(surface)        
   # End setup_surfaces

   @classmethod
   def setup_sound(cls):
      cls.sound = pygame.mixer.Sound("sounds/heal.mp3")

   # end setup method

   def apply_efffect(n:Ninja):
      n.update_lives(1)
      Aid.sound.play()
   # end apply effect method
# end class Aid



class Treasure(Falling_Object):
   sound = None
   surface_list = None
   prize_list =None
  
   
   def __init__(self, rec:pygame.Rect,vel, acc):

      if not Treasure.sound:
         Treasure.setup_sound()
      # end if not Treasure.s

      if not Treasure.surface_list:
         Treasure.setup_surfaces(*rec.size)

      # random select a surf from surface_list
      i = random.randint(0,2)
      super().__init__(rec, Treasure.surface_list[i], vel, acc)

   @classmethod
   def setup_surfaces(cls,treasure_w, treasure_h):
      cls.surface_list = [pygame.transform.scale(pygame.image.\
                     load(f"pics/treasure_{i}.png"),(treasure_w,\
                                                 treasure_h)) \
                     for i in range(1,4)
      ]
   # End setup_surfaces

   @classmethod
   def setup_sound(cls):
      cls.sound = pygame.mixer.Sound("sounds/coin.mp3")

   # end setup method

   def apply_efffect(n:Ninja):
      
      n.update_score(1)
      Treasure.sound.play()
   # end apply effect method
# end class Treasure

if __name__ == "__main__":
   pygame.init()
   screen  = pygame.display.set_mode((800,600))
   rec= pygame.Rect(0,0,25,25)
   surface = pygame.image.load("pics/bomb_1.png")
   f = Bomb(rec,surface, vel=5,acc=1)
   print(f)
  
  