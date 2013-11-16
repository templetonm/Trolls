from weapon import Weapon

LEVEL1_DAGGER = Weapon("Dagger", 4, toHit=1, initiative=-2, grapple=2)
LEVEL2_DAGGER = Weapon("Dagger", 4, toHit=2, initiative=-2, grapple=2)
LEVEL3_DAGGER = Weapon("Dagger", 4, toHit=3, initiative=-2, grapple=4, damage=1)

LEVEL1_SHORT_SWORD = Weapon("Short Sword", 6, toHit=1)
LEVEL2_SHORT_SWORD = Weapon("Short Sword", 6, toHit=2)
LEVEL3_SHORT_SWORD = Weapon("Short Sword", 6, toHit=3, meleeDefense=1)

LEVEL1_ELVEN_LONG_SWORD = Weapon("Elven Long Sword", 8, toHit=1, toHitMetal=-1,
    woundPenalty=-1)
LEVEL2_ELVEN_LONG_SWORD = Weapon("Elven Long Sword", 8, toHit=2, toHitMetal=-1,
    woundPenalty=-1)
LEVEL3_ELVEN_LONG_SWORD = Weapon("Elven Long Sword", 8, toHit=3, toHitMetal=-1,
    woundPenalty=-1, meleeDefense=1)

LEVEL1_GHENDISH_LONG_SWORD = Weapon("Ghendish Long Sword", 8, toHit=1)
LEVEL2_GHENDISH_LONG_SWORD = Weapon("Ghendish Long Sword", 8, toHit=2)
LEVEL3_GHENDISH_LONG_SWORD = Weapon("Ghendish Long Sword", 8, toHit=3,
    meleeDefense=1)

LEVEL1_DELENESE_BROAD_SWORD = Weapon("Delenese Broad Sword", 10, toHit=1,
    breakPoints=1)
LEVEL2_DELENESE_BROAD_SWORD = Weapon("Delenese Broad Sword", 10, toHit=2,
    breakPoints=1)
LEVEL3_DELENESE_BROAD_SWORD = Weapon("Delenese Broad Sword", 10, toHit=3,
    breakPoints=1, meleeDefense=1)

LEVEL1_CAYTHIAN_GREAT_SWORD = Weapon("Caythian Great Sword", 12, toHit=1,
    breakPoints=1)
LEVEL2_CAYTHIAN_GREAT_SWORD = Weapon("Caythian Great Sword", 12, toHit=2,
    breakPoints=1)
LEVEL3_CAYTHIAN_GREAT_SWORD = Weapon("Caythian Great Sword", 12, toHit=3,
    breakPoints=1, meleeDefense=1)

LEVEL1_DORRAN_CLEAVER = Weapon("Dorran Cleaver", 6, toHit=1, toHitMetal=1)
LEVEL2_DORRAN_CLEAVER = Weapon("Dorran Cleaver", 6, toHit=2, toHitMetal=1)
LEVEL3_DORRAN_CLEAVER = Weapon("Dorran Cleaver", 6, toHit=3, toHitMetal=1,
    meleeDefense=1)
