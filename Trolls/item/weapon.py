from armor import ARMOR_TYPE_METAL

class Weapon(object):
    def __init__(self, name, damage, initiative=0, grapple=0, bonusDamage=0,
                 meleeDefense=0, woundPenalty=0, toHit=0, toHitLeather=0,
                 toHitMetal=0, breakPoints=0):
        self._name = name
        self._damage = damage
        self._initiative = initiative
        self._grapple = grapple
        self._bonusDamage = bonusDamage
        self._meleeDefense = meleeDefense
        self._woundPenalty = woundPenalty
        self._toHit = toHit
        self._toHitLeather = toHitLeather
        self._toHitMetal = toHitMetal
        self._breakPoints = breakPoints

    def getMeleeDefense(self):
        return self._meleeDefense

    def getToHit(self, armorType=None):
        toHit = self._toHit
        if armorType is not None and armorType == ARMOR_TYPE_METAL:
            toHit += self._toHitMetal
        else:
            toHit += self._toHitLeather

        return toHit

    def getBreakPoints(self):
        return self._breakPoints
