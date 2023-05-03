

The hand-insert task requires the robot to pick up a puck and then move it to a target location. The steps necessary are as follows: 

1. Put gripper above the puck
2. Drop gripper around the puck
3. Close gripper around the puck
4. Move puck to the target location

```
# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to target location
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("vertically aligned with the puck")
    # If the puck is below the robot's gripper and the gripper is closed, we can
    # move the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is closed"):
        robot.move_gripper("near target location")