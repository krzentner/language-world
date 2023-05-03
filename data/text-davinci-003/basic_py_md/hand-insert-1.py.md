

Then, your code would be:

```
# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is not near target and the robot's gripper is closed"):
        robot.move("gripper to target")
    if check("the robot's gripper is near target"):
        robot.place("puck at target")
```