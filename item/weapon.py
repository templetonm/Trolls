import random

from armor import ARMOR_TYPE_LEATHER, ARMOR_TYPE_METAL

class Weapon(object):
    def __init__(self, name, damage, initiative=0, grapple=0, bonusDamage=0,
                 meleeDefense=0, woundPenalty=0, toHit=0,
                 breakPoints=0, leatherBreakPoints=0, metalBreakPoints=0):
        self._name = name
        self._damage = damage
        self._initiative = initiative
        self._grapple = grapple
        self._bonusDamage = bonusDamage
        self._meleeDefense = meleeDefense
        self._woundPenalty = woundPenalty
        self._toHit = toHit
        self._breakPoints = breakPoints
        self._leatherBreakPoints = leatherBreakPoints
        self._metalBreakPoints = metalBreakPoints

    @property
    def name(self):
        return self._name

    @property
    def initiative(self):
        return self._initiative

    @property
    def grapple(self):
        return self._grapple

    @property
    def meleeDefense(self):
        return self._meleeDefense

    @property
    def woundPenalty(self):
        return self._woundPenalty

    def doHit(self, defense, armor=None):
        # roll a D6
        result = random.randint(1,6)

        # TODO: Feats

        if result == 1:
            return False

        # add the weapon skill to-hit chance (accuracy)
        result += self._toHit

        # add break points if necessary
        if armor is not None and armor.armorType is not None:
            # generic break points such as using a weapon with two hands
            result += self._breakPoints

            # add in specific armor penetrating advantages
            if armor.armorType == ARMOR_TYPE_METAL:
                result += self._metalBreakPoints
            elif armor.armorType == ARMOR_TYPE_LEATHER:
                result += self._leatherBreakPoints

        if result >= defense:
            return True
        else:
            return False

    def doDamage(self, characterDamage=0):
        # roll for damage
        result = random.randint(1, self._damage)

        # TODO: Wounds

        # add weapon bonus damage
        result += self._bonusDamage

        # add character bonus damage
        result += characterDamage

        return result
