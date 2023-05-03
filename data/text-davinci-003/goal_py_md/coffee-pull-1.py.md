

Then, add the code to the function:

```
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps: 
    # 1. Put gripper around mug handle 
    # 2. Close gripper around mug handle
    # 3. Pull the mug to the target location 

    # If the gripper isn't near the mug handle, move it near the handle.
    if check("the robot's gripper is not near the mug handle"):
        robot.move_gripper("near the mug handle")
        
    # Once the gripper is near the mug handle, close the gripper around the handle.
    if check("the robot's gripper is close to the mug handle"):
        robot.move_gripper("around the mug handle", close_gripper=True)

    # If the gripper is around the mug handle and the mug is not at the 
    # target location, pull the mug towards the target location.
    if check("the robot's gripper is around the mug handle and the mug is not at the target location"):
        robot.move_gripper("near the target location")
```