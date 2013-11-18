BASE_LIFE = 20
BASE_EVASION= 3

LIFE_FROM_BUILD = {
    8: 40,
    7: 35,
    6: 30,
    5: 25,
    4: 20,
    3: 15,
    2: 10,
    1: 5,
    0: 0,
    -1: -5,
    -2: -8,
    -3: -11,
    -4: -14,
    -5: -15,
    -6: -16,
}

DAMAGE_FROM_SRENGTH = {
    8: 4,
    7: 3,
    6: 3,
    5: 2,
    4: 2,
    3: 1,
    2: 1,
    1: 0,
    0: 0,
    -1: 0,
    -2: -1,
    -3: -1,
    -4: -2,
    -5: -2,
    -6: -3,
}

BREAK_POINTS_FROM_BUILD = {
    8: 2,
    7: 2,
    6: 1,
    5: 1,
    4: 0,
    3: 0,
    2: 0,
    1: 0,
    0: 0,
    -1: 0,
    -2: 0,
    -3: -1,
    -4: -1,
    -5: -2,
    -6: -2,
}

DAMAGE_FROM_DEXTERITY = {
    5: 4,
    4: 4,
    3: 3,
    2: 2,
    1: 1,
    0: 0,
    -1: 0,
    -2: -1,
    -3: -1,
    -4: -2,
}

EVASION_FROM_DEXTERITY = {
    5: 2,
    4: 2,
    3: 1,
    2: 1,
    1: 0,
    0: 0,
    -1: 0,
    -2: -1,
    -3: -1,
    -4: -2,
}

class Character(object):
    def __init__(self, name, build, dexterity, intelligence, armor=None,
                weapons=None, strength=0, life=0, fortitude=0):
        self._name = name
        self._build = build
        self._dexterity = dexterity
        self._intelligence = intelligence
        self._armor = armor
        self._weapons = weapons
        # total strength is build plus bonus strength
        self._strength = build + strength
        # total life is base life plus build-based life plus bonus life
        self._life = BASE_LIFE + LIFE_FROM_BUILD[self._build] + life
        # total fortitude is build plus bonus fortitude
        self._fortitude = build + fortitude
        self._initiative = dexterity
        # total evasion is base evasion plus dexterity-based evasion
        self._evasion = BASE_EVASION + EVASION_FROM_DEXTERITY[self._dexterity]
        # initial break points is build-based break points
        self._breakPoints = BREAK_POINTS_FROM_BUILD[self._build]
        # initial damage is strength-based damage plus dexterity-based damage
        self._damage = DAMAGE_FROM_SRENGTH[self._strength] + \
                DAMAGE_FROM_DEXTERITY[self._dexterity]

    @property
    def evasion(self):
        return self._evasion

    @property
    def meleeDefense(self):
        return self._armor.meleeDefense

    @property
    def rangedDefense(self):
        return self._armor.rangedDefense

    def printStats(self):
        print """Name: {}
Life: {:+d}
Defense Value (Melee): {:+d}
Defense Value (Ranged): {:+d}
Build: {:+d}
Dexterity: {:+d}
Intelligence: {:+d}
Initiative: {:+d}
Break Points: {:+d}
To Hit: {:+d}
Strength: {:+d}
Fortitude: {:+d}
Damage: {:+d}""".format(
            self._name, self._life, self._meleeDefense, self._rangedDefense,
            self._build, self._dexterity, self._intelligence, self._initiative,
            self._breakPoints, self._toHit, self._strength, self._fortitude,
            self._damage)

    def attack(self, weapon, enemy):
        # first see if it hits
        if weapon.doHit(enemy.enemyDefense, enemyArmor):
            print "Hit"

            # roll for damage, perform feats and add in character bonus damage
            damage = weapon.doDamage(self._damage)

        else:
            print "Missed"

    def takeDamage(self, damage):
        self._life -= damage

        print "Lost {} life".format(damage)
