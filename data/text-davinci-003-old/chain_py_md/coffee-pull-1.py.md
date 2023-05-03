

The program should be:

```
# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    # 1. Put the gripper above the mug
    # 2. Lower the gripper around the mug
    # 3. Close the gripper around the mug
    # 4. Pull the mug to the target location
    # First, put the gripper roughly above the mug.
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    # Once the gripper is lined up above the mug, we should be able to grab the 
    # mug by moving the gripper down and around it.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # Once the gripper is around the mug, we can just close the gripper to grab it.
    if check("the robot's gripper is around mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # We closed the gripper, and the mug is still near the gripper, so maybe we
    # grabbed it. Try to move the mug to the goal.   
    if check("the robot's gripper is above mug and the robot's gripper is closed"):
        robot.pull("mug to goal")
```