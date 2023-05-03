

Under the `pick_out_of_hole` function, add the following code:

```
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.grab("peg")
    if check("the robot's gripper is near peg and the peg is not above the robot's gripper"):
        robot.pull("peg up")
    if check("the peg is above the robot's gripper"):
        robot.close("gripper around peg")
    if check("the robot's gripper is above the target location and the robot's gripper is closed"):
        robot.place("peg at goal")
```