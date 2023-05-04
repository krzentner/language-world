

```
# hammer: hit the nail with the hammer
def hammer(robot):
    if check("the robot's gripper is not vertically aligned with the nail and the robot's gripper is not near the nail"):
        robot.move("gripper to the nail")
    if check("the robot's gripper is vertically aligned with the nail and the robot's gripper is not near the nail"):
        robot.push("gripper down to the nail")
    if check("the robot's gripper is around the nail and the robot's gripper is not vertically aligned with the hammer"):
        robot.push("gripper to the hammer")
    if check("the robot's gripper is vertically aligned with the hammer and the robot's gripper is not near the hammer"):
        robot.move("gripper to the hammer")
    if check("the robot's gripper is vertically aligned with the hammer and the robot's gripper is near the hammer"):
        robot.push("hammer against the nail")
```

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. If the gripper is not vertically aligned with the nail, put it above the nail
    #  2. If the gripper is vertically aligned with the nail but not near the nail, push the gripper down to the nail
    #  3. If the gripper is vertically aligned with the hammer but not near the hammer, move the gripper to the hammer
    #  4. If the gripper is around the nail and not vertically aligned with the hammer, put it above the hammer
    #  5. If the gripper is vertically aligned with the hammer, push the hammer against the nail
    # If the robot's gripper is not vertically aligned with the nail and the robot's gripper is not near the nail
    if check("the robot's gripper is not vertically aligned with the nail and the robot's gripper is not near the nail"):
        robot.move("gripper to the nail")
    # If the robot's gripper is vertically aligned with the nail and the robot's gripper is not near the nail
    if check("the robot's gripper is vertically aligned with the nail and the robot's gripper is not near the nail"):
        robot.push("gripper down to the nail")
    # If the robot's gripper is vertically aligned with the hammer and the robot's gripper is not near