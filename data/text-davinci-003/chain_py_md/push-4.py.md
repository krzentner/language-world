

Add the code:

```
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper against edge of puck right side
    #  2. Push the puck to the right side
    #  3. Push the puck to the target location

    # Move the gripper to the right edge of the puck. This way, when we push,
    # the puck will move to the right.
    if check("the robot's gripper is not left of puck and the robot's gripper is not above puck"):
        robot.move("gripper to right of puck")
    # Once the gripper is to the right of the puck, start pushing the puck. 
    if check("the robot's gripper is left of puck"):
        robot.push("puck to the right")
    # Keep pushing the puck to the right until it reaches the target.
    if check("puck is not at the target"):
        robot.push("puck to the target")
```