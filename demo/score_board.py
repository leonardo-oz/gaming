import pygame

class ScoreBoared:



  def __init__(self, b_rec: pygame.Rect):
    self.board_rec = b_rec
    self.textFont = pygame.font.SysFont("Arial",36)
    self.score_color = (255,0,0)

    pass



  def draw(self, canvas: pygame.Surface, score: int):
    # draw a number of lives 
    text_surface = self.textFont.render(f"score: {score}",True,self.score_color)
    canvas.blit(text_surface,self.board_rec)
  # End method
