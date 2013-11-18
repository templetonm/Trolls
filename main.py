from character.character import Character
from item import items
from item.armor import Armor
from item.weapon import Weapon

if __name__ == "__main__":
    # Thorbjorn
    thorbjorn = Character("Thorbjorn", 2, 2, -1)
    thorbjorn.printStats()
    xavier = Character("Xavier", 2, 1, 1)
    xavier.printStats()
    thorbjorn.attack(items.LEVEL3_DAGGER, xavier)
