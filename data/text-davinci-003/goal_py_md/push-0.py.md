

Then complete the program.

```
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper near the puck
    #  2. Push the puck to the target location
    # First, if the gripper isn't near the puck to start pushing it, line up the
    # gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the robot's gripper is above the puck, drop the gripper around it and
    # start pushing.
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Now that the gripper is around the puck, start pushing it towards the
    # target.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("near the target location")
```