

Steps: 
  1. Put the gripper above the mug handle
  2. Grab the mug handle with the gripper
  3. Move the mug to the target location

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Grab the mug handle with the gripper
    #  3. Move the mug to the target location
    # We can grab the mug handle by lining the gripper up above it.
    if check("the robot's gripper is not above the mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is aligned with the mug handle, close it to grab the mug
    # handle.
    if check("the robot's gripper is above the mug handle"):
        robot.close("gripper around mug handle")
    # We can move the mug to the target location as long as the gripper is closed
    # around the mug handle.
    if check("the robot's gripper is closed around mug handle"):
        robot.move("mug to target location")
```