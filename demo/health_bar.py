import pygame

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


if __name__ == "__main__":
  rec = pygame.Rect(10,10,100,20)
  h = Health_Bar(rec,0.25)
  h.update()
  print(h)
