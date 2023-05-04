

Steps:
- 1. Put gripper above mug
- 2. Drop gripper around mug
- 3. Close gripper around mug
- 4. Pull mug to goal

Now, fill in the robot motion commands to complete the task.

##### Input IDs:
#####   `robot`

##### Expected Output IDs:
#####   `coffee-pull`

###### Answer:

# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
# Steps:
#  1. Put gripper above mug
#  2. Drop gripper around mug
#  3. Close gripper around mug
#  4. Pull mug to goal
# Put the gripper above mug
if check("the robot's gripper is not vertically aligned with the mug"):
    robot.move_gripper("vertically aligned with the mug")
# Drop gripper around mug
if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around the mug"):
    robot.move_gripper("near the mug")
# Close gripper around mug
if check("the robot's gripper is above the mug"):
    robot.move_gripper("near the mug", close_gripper=True)
# Pull mug to goal
if check("the robot's gripper is below the mug"):
    robot.move_gripper("forward aligned with mug")
"""
[eod] [code]import csv
import re

from . import _make_id, _split

_TYPE_RE = re.compile("(?P<type>[a-z]*): (?P<title>.*)")


class _Row:

    def __init__(self, csvrow, title_offset=None, **kwargs):
        self.id = _make_id(csvrow[1])

        if 'data_url' not in kwargs:
            data_url = csvrow[3]
            self.data_url = _split(data_url, separator=',')
        else:
            self.data_url = kwargs.pop('data_url')

        if 'data' not in kwargs:
            self.data = csvrow[4:]
        else:
            self.data = kwargs.pop('data')

        if not title_offset and 'title_offset' not in kwargs:
            self.title = csvrow[2]