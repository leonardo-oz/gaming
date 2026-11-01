import pygame
import random
from abc import ABC, abstractmethod
from ninja import Ninja
from explosive import Explosive

class Falling_Object(pygame.sprite.Sprite,ABC):
	def __init__(self,rec, bomb_surface, vel,acc):
		super().__init__()
		self.rect = rec
		self.image = bomb_surface
		self.vel = vel
		self.acc = acc
	# End __init__ method

	def __str__(self):
		return f"{self.__class__.__name__} at at {self.rec.x},{self.rec.y}, moving speed: {self.vel}"


	def update(self, screen_height):
		self.rect.y += self.vel
		self.vel += self.acc
		if self.rect.y >= screen_height:
			self.kill()
		# end if
	# end update method

	@abstractmethod
	def apply_effect(self,player):
	  pass

# End Falling_Object Class

class Bomb(Falling_Object):
	# ========== class variables ==========
	surfaces: list[pygame.Surface] = []
	sound: pygame.mixer.Sound = None
	explosive_frames: list[pygame.Surface] =[]
	explosive_group: pygame.sprite.Group = None

	@classmethod
	def setup_resources(
		cls,
		surfaces: list[pygame.Surface],
		sound: pygame.mixer.Sound,
		frames: list[pygame.Surface],
		group: pygame.sprite.Group
	):

		cls.surfaces = surfaces
		cls.sound = sound
		cls.explosive_frames = frames
		cls.explosive_group = group

	# End setup_resources method

	def __init__(self, screen_width: int,
						bomb_width: int = 50, bomb_height: int = 50):
		surface = random.choice(Bomb.surfaces)
		x_pos = random.randint(0,screen_width-bomb_width-1)
		rec = pygame.Rect(x_pos,0,bomb_width,bomb_height)
		vel = random.randint(1,4)
		acc = random.uniform(0,1)
		super().__init__(rec, surface, vel, acc)

	# End __init__ method

	def apply_effect(self,player:Ninja):
		if not player.is_alive:
			return

		player.update_lives(-1)

		if Bomb.sound:
			Bomb.sound.play()

		if Bomb.explosive_group and Bomb.explosive_frames:
			# infer explosive dimension from 1st frame
			exp_w, exp_h = Bomb.explosive_frames[0].get_size()
			exp_rec = pygame.Rect(self.rec.x, self.rec.y,exp_w,exp_h)
			Bomb.explosive_group.add(Explosive(exp_rec,Bomb.explosive_frames))

# End Bomb Class

class Aid(Falling_Object):
	surfaces: list[pygame.Surface]=[]
	sound: pygame.mixer.Sound = None

	@classmethod
	def setup_resources(
		cls,
		surfaces: list[pygame.Surface],
		sound: pygame.mixer.Sound
	):
		cls.surfaces=surfaces
		cls.sound = sound

	# End setup_resources method

	def __init__(self, screen_width: int,
						 aid_width: int = 50, aid_height: int = 50
					):

		surface = random.choice(Aid.surfaces)
		x_pos = random.randint(0,screen_width-aid_width-1)
		rec = pygame.Rect(x_pos,0,aid_width,aid_height)
		vel = random.randint(1,4)
		acc = random.uniform(0,1)
		super().__init__(rec, surface, vel, acc)
	# End __init__ method

	def apply_effect(self, player: Ninja):
		if not player.is_alive or player.num_of_lives == Ninja.MAX_LIVES:
			return
		player.update_lives(1)
		if Aid.sound:
			Aid.sound.play()
# End Aid class

class Treasure(Falling_Object):
	surfaces: list[pygame.Surface]=[]
	sound: pygame.mixer.Sound = None

	@classmethod
	def setup_resources(
			cls,
			surfaces: list[pygame.Surface],
			sound: pygame.mixer.Sound
	):
		cls.surfaces=surfaces
		cls.sound = sound

	# End setup_resources method

	def __init__(self, screen_width: int,
	             treasure_width: int = 50,
				 treasure_height: int = 50
				):
		surface_idx = random.randrange(len(Treasure.surfaces))
		surface = Treasure.surfaces[surface_idx]
		x_pos = random.randint(0,screen_width-treasure_width-1)
		rec = pygame.Rect(x_pos,0,treasure_height,treasure_height)
		vel = random.randint(1,4)
		acc = random.uniform(0,1)
		super().__init__(rec, surface, vel, acc)
		self.prize = (surface_idx+1)*10
	# End __init__ method

	def apply_effect(self, player: Ninja):
		if not player.is_alive:
			return
		player.update_score(self.prize)
		if Treasure.sound:
			Treasure.sound.play()
	# End apply_effect method

# End Treasure class

if __name__ == "__main__":
  pass
