

Then finish the program:

```
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Line up the gripper with the puck
    #  2. Push the puck to the goal
    # First, make sure the robot's gripper is horizontally aligned with the puck.
    if check("the robot's gripper is not horizontally aligned with the puck"):
        robot.align("gripper to puck")
    # Now that the gripper is in line with the puck, we can push the puck to the goal.
    if check("the robot's gripper is horizontally aligned with the puck"):
        robot.push("puck to goal")
```