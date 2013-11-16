BASE_LIFE = 20
BASE_DEFENSE = 3

NEG_BUILD_LIFE = {
    -1: -5,
    -2: -8,
    -3: -11,
    -4: -14,
    -5: -15,
    -6: -16,
}

class Character(object):
    def __init__(self, name, build, dexterity, intelligence, weapons,
                 strength=0, life=0, armor=0, fortitude=0):
        self._name = name
        self._build = build
        self._dexterity = dexterity
        self._intelligence = intelligence
        self._weapons = weapons
        self._strength = strength + build
        self._life = life + BASE_LIFE
        self._fortitude = fortitude + build
        self._initiative = dexterity
        self._defense = armor + BASE_DEFENSE
        self._toHit = 0
        self._breakPoints = 0
        self._damage = 0

        # Compute life
        if build >= 0:
            self._life += int(5 * build)
        else:
            self._life += NEG_BUILD_LIFE[build]

        # Compute break points
        if build >= 5:
            self._breakPoints += int((build-3)/2)
        elif build <= -3:
            self._breakPoints += int((build+2)/2)

        # Compute strength based damage
        if strength >= 0:
            self._damage += int(strength/2)
        else:
            self._damage += int((strength+1)/2)

        # Compute dexterity based damage
        if dexterity >= 0:
            self._damage += min(dexterity, 4)
        elif dexterity <= -2:
            self._damage += int((dexterity+1)/2)

        # Compute dexterity based defense value
        if dexterity >= 0:
            self._defense += int(dexterity/2)
        else:
            self._defense += int((dexterity+1)/2)

        self._rangedDefense = self._defense
        self._meleeDefense = self._defense

    def printStats(self):
#         for weapon in self._weapons:
#             print "Weapon(s): {}".format(" and ".join(self._weapons))

        print """Name: {}
Life: {:+d}
Defense Value (Melee): {:+d}
Defense Value (Ranged): {:+d}
Build: {:+d}
Dexterity: {:+d}
Intelligence: {:+d}
Initiative: {:+d}
To-Hit: {:+d}
Strength: {:+d}
Fortitude: {:+d}
Damage: {:+d}""".format(
            self._name, self._life, self._meleeDefense, self._rangedDefense, self._build, self._dexterity,
            self._intelligence, self._initiative, self._toHit, self._strength,
            self._fortitude, self._damage)
