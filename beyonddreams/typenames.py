# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software: you can redistribute it and/or modify     #
#     it under the terms of the GNU General Public License as published by     #
#     the Free Software Foundation, either version 3 of the License, or        #
#     (at your option) any later version.                                      #
#                                                                              #
#     This program is distributed in the hope that it will be useful,          #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#     GNU General Public License for more details.                             #
#                                                                              #
#     You should have received a copy of the GNU General Public License        #
#     along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Non-Elementals
PHYS =      "physical"
PSYC =      "psychic"
SPIR =      "spirit"
NON_ELEMS =   PHYS, SPIR, PSYC

# Elements
FIRE =      "fire"
ICE =       "ice"
WATER =     "water"
WIND =      "wind"
ELEC =      "electric"
LIGHT =     "light"
DARK =      "dark"
MAG =       "magnetic"
ELEMS =     FIRE, ICE, WATER, WIND, ELEC, LIGHT, DARK, MAG

# ---- Stats ----------------------------------------------------------------- #
HP =        "health"
WIL =       "willpower"
INT =       "intellect"
STR =       "strength"
FOC =       "focus"
STA =       "stamina"
LUC =       "luck"
KAR =       "karma"
STATS = HP, WIL, INT, STR, FOC, STA, LUC, KAR

# Stat Groups
#PHYS =      "physical"
MNTL =      "mental"
STAT_GROUPS = PHYS, MNTL

# ---- Statuses -------------------------------------------------------------- #
# Groups
MIND =      "mind"
TFORM =     "transform"
MUTA =      "mutation"
SENS =      "sensory"
SPD =       "speed"
UNDEAD =    "undead"
WOUND =     "wound"
STATUS_GROUPS = MIND, TFORM, MUTA, SENS, SPD, WOUND

# MIND type
CONFU =     "confusion"
DUMB =      "dumb"
SILENCE =   "silence"
STATUSGROUP_MIND = CONFU, DUMB, SILENCE

# WOUND type
BURN =      "burn"
FBITE =     "frostbite"
BLEED =     "bleed"
STATUSGROUP_WOUND = BURN, FBITE, BLEED

# SPD type
HASTE =     "haste"
SLOW =      "slow"
STATUSGROUP_SPD = HASTE, SLOW

# TFORM type
SHRINK =    "shrink"
STATUSGROUP_TFORM = SHRINK

# SENS type
BLIND =     "blind"
CONV =      "convulsion"
NUMB =      "numb"
PARA =      "para"
STUPOR =    "stupor"
STATUSGROUP_SENS = BLIND, CONV, NUMB, PARA, STUPOR

# HEX type
CURSED =    "cursed"
HEXED =     "hexed"
JINXED =    "jinxed"
HNULL =     "heal null"
STATUSGROUP_HEX = CURSED, HEXED, JINXED, HNULL

ZOMBIFY =   "zombify"
ZOMBIE =    "zombie"
STATUSGROUP_UNDEAD = ZOMBIFY, ZOMBIE

POISON =    "poison"
DRUNK =     "drunk"
EXAUST =    "exaustion"
HALLU =     "hallucination"
RADIA =     "radia"

RAGE =      "rage"
BLUST =     "blood lust"
ADREN =     "adrenalin"

UNGROUPED_STATUSES = (POISON, DRUNK, EXAUST, HALLU, RADIA, RAGE, BLUST, ADREN)
GROUPED_STATUSES = (STATUSGROUP_MIND + STATUSGROUP_SENS + STATUSGROUP_SPD +
    STATUSGROUP_TFORM + STATUSGROUP_HEX + STATUSGROUP_UNDEAD + STATUSGROUP_WOUND)
ALL_STATUS_NAMES = GROUPED_STATUSES + UNGROUPED_STATUSES

# ---- Family Types ---------------------------------------------------------- #
BEAST =     "beast"
INSECT =    "insectoid"
REPT =      "reptillion"
PLANT =     "plant"
SLIME =     "slime"
MECH =      "mech"
PFAMS =     BEAST, INSECT, REPT, PLANT, SLIME, MECH

AQUA =     "aquatic"
FLYING =   "flying"
SPIRIT =    SPIR
SFAMS =     AQUA, FLYING, POISON, UNDEAD, SPIR

# ---- Abbr ------------------------------------------------------------------ #
ABBRS = {
    # stats
    HP:     "HP",
    SPD:    "SPD",
    MNTL:   "MNTL",

    # status
    EXAUST: "EXAUST",
    HALLU:  "HALLU",
    ADREN:  "ADREN",
    BLUST:  "BLUST",
    FBITE:  "FBITE",
    HNULL:  "HNULL",
    CONFU:  "CONFU",

    # elem
    MAG:    "MAG",
}

ABBRS_TRIM_TO_4 = ELEC, CONV, PARA, MUTA, SENS, PHYS, SPIR, PSYC
