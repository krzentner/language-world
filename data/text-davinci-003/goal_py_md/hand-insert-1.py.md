

Then, write the code to control the robot:

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
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("over the puck", press_down=True)
    # If the puck has been trapped, move it to the target location.
    if check("the robot's gripper is over the puck"):
        robot.move_gripper("near the target location")
```