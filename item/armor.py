ARMOR_TYPE_LEATHER = "Leather"
ARMOR_TYPE_METAL = "Metal"

class Armor(object):
    def __init__(self, name, armorType=None, meleeDefense=0, rangedDefense=0,
            leftArm=None, leftLeg=None, rightArm=None, rightLeg=None,
            torso=None, head=None):
        self._name = name
        self._armorType = armorType
        self._meleeDefense = meleeDefense
        self._rangedDefense = rangedDefense
        self._head = head
        self._leftArm = leftArm
        self._leftLeg = leftLeg
        self._rightArm = rightArm
        self._rightLeg = rightLeg
        self._torso = torso

    @property
    def armorType(self):
        return self._armorType

    def getMeleeDefense(self):
        return self._meleeDefense

    def getRangedDefense(self):
        return self._rangedDefense

    def defendWound(self, woundPenalty=0):
        pass
