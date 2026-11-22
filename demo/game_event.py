import pygame



class GameEvent():
  SPAWN_BOMB_EVENT = pygame.USEREVENT + 1
  SPAWN_AID_EVENT = pygame.USEREVENT +2 
  SPAWN_TREASURE_EVENT = pygame.USEREVENT +3 
  BOMB_EXPLODED_EVENT = pygame.USEREVENT +4
