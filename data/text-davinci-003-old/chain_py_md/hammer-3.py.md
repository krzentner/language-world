

Steps:
1. Put the gripper above the nail 
2. Drop the gripper around the nail 
3. Move the gripper forward to hit the nail with hammer 
4. Pull the gripper back

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the gripper above the nail
    #  2. Drop the gripper around the nail
    #  3. Move the gripper forward to hit the nail with hammer
    #  4. Pull the gripper back
    if check("the robot's gripper is not above the nail"):
        robot.put("gripper above nail")
    if check("the robot's gripper is not around the nail and the robot's gripper is open"):
        robot.drop("gripper around nail")
    if check("the robot's gripper is near the nail and the robot's gripper is open"):
        robot.move("gripper forward to hit nail with hammer")
    if check("the robot's gripper is near nail and the robot's gripper is closed"):
        robot.pull("gripper back")
``