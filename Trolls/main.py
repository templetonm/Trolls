from character.character import Character
from item.weapon import Weapon

if __name__ == "__main__":
    # Thorbjorn
    character = Character("Thorbjorn", 2, 2, -1, None, armor=4)
    character.printStats()
