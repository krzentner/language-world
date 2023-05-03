Here's the solution to perform the task `pick-place`.

```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.grab("puck")
    if check("the robot's gripper is holding the puck"):
        robot.put("gripper above goal")

```

This code uses the `put` and `grab` methods to control the robot's gripper position. It first checks if the gripper is vertically aligned with the puck and if not, positions the gripper above it. Next, it checks if the gripper is holding the puck and if not, it grabs the puck. Finally, the program moves the gripper to the target location and holds the puck there.