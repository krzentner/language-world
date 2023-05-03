

Then, write a program to complete the task:

```
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #   1. Put gripper above mug handle
    #   2. Grab the mug handle with the gripper
    #   3. Push the mug to the target location
    
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not vertically aligned with the mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is aligned with the mug handle, move the gripper down 
    # around it to grab the handle.
    if check("the robot's gripper is vertically aligned with the mug handle and the robot's gripper is not around mug handle"):
        robot.put("gripper around mug handle")
    # Once the gripper is around the handle, push it towards the goal.
    if check("the robot's gripper is around mug handle"):
        robot.push("mug to goal")
```