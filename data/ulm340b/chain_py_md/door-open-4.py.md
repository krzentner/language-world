

You can use the following commands, some of which use objects like the robot's gripper and objects in the environment:

- `robot.put(object1, preposition, object2)`, puts `object1` onto `object2`.
    Some possible prepositions are: "above", "below", "left-of", "right-of", "on-top-of".

- `robot.place(object1, preposition, object2)`, places `object1` onto `object2` gently.

- `robot.move(object1, preposition, object2)`, moves `object1` to near `object2`.
    Unlike `put` or `place`, this doesn't imply contact.

- `robot.grab(object)`, grabs `object`.

- `robot.drop(object)`, drops `object`.

- `robot.close(object)`, closes `object`.

- `robot.open(object)`, opens `object`.

- `robot.pull(object)`, pulls `object`.

- `robot.push(object)`, pushes `object`.

- `robot.insert(object1, preposition, object2)`, inserts `object1` into `object2`.
    For example, insert "peg" into "hole".

- `robot.align(object1, preposition, object2)`, aligns `object1` to `object2`.
    Some possible prepositions are: "above", "below", "on-top-of", "beside", "behind", "in-front-of", "left-of", "right-of".

- `robot.slide(object1, preposition, object2)`, slides `object1` along `object2`.
    Some possible prepositions are: "above", "below", "on-top-of", "beside", "behind", "in-front-of", "left-of", "right-of".

Please write the function `door_open`.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from builtins import *
from future import *


def door_open(robot):
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # We need to put the gripper above the door handle before we can grab it,
    # because