import pygame

class Explosive(pygame.sprite.Sprite):

    explosive_surface_list = None

    def __init__(self, rec:pygame.rect.Rect):
        super().__init__()
        self.rect = rec
        self.curr_i = 0
        if not Explosive.explosive_surface_list:
            Explosive._create_explosive_surface_list(*rec.size)
        # if not explosive_surface_list:
        self.image = Explosive.explosive_surface_list[0]
    # End method __init__


    def __str__(self):
        return f"position at {self.rect.x},{self.rect.y}, image  position: {self.curr_i}"

    def update(self):
        if self.curr_i >= len(Explosive.explosive_surface_list):
            self.kill()
        else:
            self.image = Explosive.explosive_surface_list[self.curr_i]
            self.curr_i+=1
    # End method update

    @classmethod
    def _create_explosive_surface_list(cls,w,h,num_repeats=1):
        cls.explosive_surface_list = []
        for i in range(0,4):
            for j in range(0,num_repeats):
                explosive_surface_raw = pygame.image.load(f"pics/explosive_{i}.png")
                explosive_surface = pygame.transform.scale(explosive_surface_raw,(w,h))
                cls.explosive_surface_list.append(explosive_surface)
    # End method


# explosive_surface_list = []

# End class

if __name__ == "__main__":
    pygame.init()
    screen  = pygame.display.set_mode((800,600))

    explosive_rec= pygame.Rect(0,0,25,25)
    explosive_surface_list = []
    explosive = Explosive(explosive_rec)
    print(explosive)