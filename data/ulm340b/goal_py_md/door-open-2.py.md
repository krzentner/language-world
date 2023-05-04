

Then write the rest.
We're looking for solutions that are easy to understand, not necessarily that
are short.
We're also looking for solutions that are general, so your code shouldn't
depend on very specific alignments of objects.

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. put gripper above door handle
    #  2. move gripper around door handle
    #  3. pull door open
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # If the gripper isn't near the door handle, move it near the door handle.
    if check("the robot's gripper is near door handle"):
        robot.move_gripper("vertically aligned with door handle")
    # Once the gripper is around the door handle, we can just pull the door open.
    if check("the robot's gripper is around door handle"):
        robot.move_gripper("horizontally aligned with the door handle")

# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot