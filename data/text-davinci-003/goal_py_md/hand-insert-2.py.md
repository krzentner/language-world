

```
# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is around the puck but not closed, close the gripper.
    if check("the robot's gripper is around the puck and the robot's gripper is not closed"):
        robot.move_gripper("closed around the puck")
    # Finally, move the puck to the target location.
    if check("the robot's gripper is closed around the puck"):
        robot.move_gripper("above the target location")
``