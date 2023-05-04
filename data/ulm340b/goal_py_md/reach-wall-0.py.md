

The robot has a gripper that it can open and close.
The robot can move its gripper, but it cannot move its base.
The gripper can only move vertically and horizontally.

#####

### Scene: `reach-wall`

#### Objects:

* ```robot```: The robot's gripper is closed at a horizontal position of ```1.0``` and a vertical position of ```4.0```.

* ```reach target```: The target location is a point at a horizontal position of ```2.0``` and a vertical position of ```2.5```.

#### Relations:

* ```reach```: The robot's gripper is in front of the target location, at a vertical offset of ```0.5``` and a horizontal offset of ```-1.0```.


"""

from text_utils import *

__doc__ = get_description(__doc__)


def reach_wall(robot):
    # Steps:
    #  1. Reach around the wall to the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location, but the wall is in the way!
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("below the reach target")

def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle")
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with