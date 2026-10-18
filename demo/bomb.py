import pygame
class Bomb:

  def __init__(self,rec, bomb_surface, vel):
      self.rec = rec
      self.bomb_surface = bomb_surface
      self.vel = vel
      self.active = True

      

  def __str__(self):
    return f"position at {self.rec.x},{self.rec.y}, moving speed: {self.vel}"

  def draw(self, canvas):
   if self.active:  
      canvas.blit(self.bomb_surface,self.rec)

  def update(self, screen_height):
      self.rec.y += self.vel
      if self.rec.y >= screen_height:
         self.active = False
      # end if
   # end method update



     

# End Class
# 
# 

if __name__ == "__main__":
   pygame.init()
   screen  = pygame.display.set_mode((800,600))
   bomb_rec= pygame.Rect(0,0,25,25)
   
   bomb_surface = pygame.image.load("pics/bomb_1.png")

   bomb = Bomb(bomb_rec,bomb_surface, vel=5)
   print(bomb)
  
  