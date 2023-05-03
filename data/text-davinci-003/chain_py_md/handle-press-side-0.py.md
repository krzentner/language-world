

Then continue with the steps as seen below: 

```
# Steps:
#  1. Line up the gripper with the handle from the side
#  2. Push down the handle from the side
# First, line up the robot's gripper with the handle from the side.
if check("the robot's gripper is not horizontally aligned with handle"):
    robot.put("gripper to side of handle")
# Once the gripper is lined up with the handle, push it down from the side.
if check("the robot's gripper is horizontally aligned with handle"):
    robot.push("handle down from side")
```