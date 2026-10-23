import pygame
from pygame.surface import Surface

class Health_Bar:

  def __init__(self, rec: pygame.Rect, delta_r: float) -> None:
    self.rec = rec
    self.health_ratio  = 1
    self.dr = delta_r
  # End constructor method

  def __str__(self):
    return f"remaining heath: {self.health_ratio:.2%}"
  # End str

  def draw(self, canvas: pygame.Surface):
    pygame.draw.rect(canvas,(255,0,0),self.rec)

    if self.health_ratio > 0:
      green_rec_width = self.rec.width*self.health_ratio
      # print(f"green_rec_width: {green_rec_width}")
      green_rec = pygame.Rect(self.rec.x,self.rec.y,green_rec_width, self.rec.height )
      pygame.draw.rect(canvas,(0,255,0),green_rec)

  # end draw method
   
  def update(self):
    self.health_ratio = max(0.0, self.health_ratio - self.dr)


# End class

class Heath_Bar_Heart:

  MAX_LIVES = 5

  def __init__(self, icon: Surface, n_lives: int, draw_x: float, draw_y: float):
    self.icon = icon
    self.num_of_lives = n_lives
    self.draw_x = draw_x
    self.draw_y = draw_y
    
    pass


  def __str__(self):
    # return number of lives remaining
    f"number of lives {self.num_of_lives}"

  def update(self,v):
    # decrement by 1 if number of remaining lives > 0
    if self.num_of_lives + v <= Heath_Bar_Heart.MAX_LIVES:
      self.num_of_lives = max(0, self.num_of_lives + v)

  def draw(self, canvas: pygame.Surface):
    # draw a number of lives 
    if self.num_of_lives > 0:  
      for i in range(self.num_of_lives):
        canvas.blit(self.icon,(self.draw_x+self.draw_x*i,self.draw_y))




if __name__ == "__main__":
  # rec = pygame.Rect(10,10,100,20)
  # h = Health_Bar(rec,0.25)
  # h.update()
  # print(h)
  heart = pygame.image.load("pics/heart.jpeg")
  heart_surface= pygame.transform.scale(heart,(20,20))

  print(heart_surface)
 