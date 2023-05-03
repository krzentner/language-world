Here's a possible solution:

```
# bin-picking: pick up the cube and place it in the target bin
def bin_picking(robot):
    if check("the robot's gripper is not near the cube"):
        robot.reach("to cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.grab("cube")
    if check("the robot's gripper is around the cube and the robot's gripper is not above the target bin"):
        robot.move("gripper above target bin")
    if check("the robot's gripper is above the target bin and the robot's gripper is closed"):
        robot.drop("cube in target bin")
```

This program uses the `reach` function to move the gripper to the cube, the `grab` function to pick up the cube, and the `move` and `drop` functions to move the cube to and drop it in the target bin. The `check` function is used to check the state of the robot and the environment before each action is performed. Note that the specific details of the movements and actions will depend on the robot's capabilities and the layout of the workspace.