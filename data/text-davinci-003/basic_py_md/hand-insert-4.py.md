

Solution:
```
# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    if check("the robot's gripper is not near the puck"):
        robot.put("gripper near puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.grab("puck")
    if check("the robot's gripper is closed around the puck"):
        robot.move("puck to target location")