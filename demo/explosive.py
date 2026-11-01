import pygame

class Explosive(pygame.sprite.Sprite):
    def __init__(self, rec, surface_list):
        super().__init__()
        self.surface_list = surface_list
        self.rect = rec
        self.curr_i = 0
        self.image = surface_list[0]
    # End method __init__


    def __str__(self):
        return f"position at {self.rect.x},{self.rect.y}, image  position: {self.curr_i}"

    def update(self):
        if self.curr_i >= len(self.surface_list):
            self.kill()
        else:
            self.image = self.surface_list[self.curr_i]
            self.curr_i+=1
    # End method update

# End class

