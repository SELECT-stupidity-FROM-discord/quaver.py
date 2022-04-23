from enum import Enum


class GameMode(Enum):
    """
    Enum for the game modes.
    """
    FOUR_KEYS:  int = 1
    SEVEN_KEYS: int = 2

    def __int__(self):
        return self.value

class RankStatus(Enum):
    """
    Enum for rank status.
    """
    UNRANKED: int = 1
    RANKED:   int = 2


    def __int__(self):
        return self.value
    
