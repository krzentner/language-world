```
# sweep-into: grab the cube and move it to the target location
# def sweep_into(robot):
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    if check("the robot's gripper is above cube and the robot's gripper is closed"):
        robot.turn("to face the target location")
    if check("the robot is facing the target location"):
        robot.move("gripper towards the target location")
    if check("the cube has been swept into the target location"):
        robot.drop("gripper to release the cube")
```