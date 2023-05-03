

Now the program:
```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.grab("the puck")
    if check("the robot's gripper is around the puck and the robot is not near the target location"):
        robot.move("gripper to the target location")
    if check("the robot's gripper is near the target location"):
        robot.place("the puck at target location")
```