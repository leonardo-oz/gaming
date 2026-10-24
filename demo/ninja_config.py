from enum import Enum, auto

class NinjaState(Enum):
  STANDING = auto() 
  RUNNING_LEFT= auto()
  RUNNING_RIGHT= auto()
  MEDITATING= auto()
  BRUCE_LEE= auto()
  DEAD= auto()
  # SOME= STANDING | RUNNING_LEFT |MEDITATING



class GameState(Enum):
  START=auto()
  PLAY= auto()  
  END=auto()


if __name__ == "__main__":
  # print(NinjaState.SOME.value)
  pass