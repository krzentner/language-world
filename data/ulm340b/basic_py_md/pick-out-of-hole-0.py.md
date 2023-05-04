

Note that, for the first time, you have not been given the program to execute. So, you will need to come up with a program that works.
"""


# Task. 8. pick-out-of-hole.
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")

    if check("the robot's gripper is above the peg and peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    
    if check("peg is horizontally aligned with hole"):
        robot.insert("gripper into hole")

    if check("peg is below the robot's gripper"):
        robot.pull("gripper up")

    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")

    if check("the robot's gripper is forward aligned with the peg"):
        robot.place("peg at goal")
[eod] [code]# -*- coding: utf-8 -*-

__title__ = 'transliterate.contrib.languages.kn'
__author__ = 'Alisue <lambdalisue@hashnote.net>'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014-2020 Alisue'

from transliterate.base import TranslitLanguagePack, registry

#: Mapping data
_mapping_data = (
    # Vowels
    (('ಅ', 'a'),),
    (('ಆ', 'aa'),),
    (('ಇ', 'i'),),
    (('ಈ', 'ii'),),
    (('ಉ', 'u'),),
    (('ಊ', 'uu'),),
    (('ಋ', 'r'),),
    (('ಎ', 'e'),),
    (('ಏ', 'ee'),),
    (('ಐ', 'ai'),),
    (('ಒ', 'o'),),
    (('ಓ', 'oo'),),
    (('ಔ', 'au'),),
    (('ಂ', 'm'),),

    # Consonants
    (('ಕ', 'ka'),),
    (('ಖ'