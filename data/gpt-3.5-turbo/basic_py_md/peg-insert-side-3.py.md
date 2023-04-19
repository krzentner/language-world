Here is the complete code for the `peg_insert_side` function:

```
# peg-insert-side: insert the peg into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        if check("the robot's gripper is not above the hole"):
            robot.lift("gripper above hole")
        if check("the robot's gripper is open"):
            robot.close("gripper around hole")
        if check("gripper is around hole and the peg is not inserted"):
            robot.insert("peg into hole")
```

This code first checks if the gripper is in the correct position to perform each step of the task. If not, it moves the gripper to the correct position using the robot's `put`, `grab`, `align`, or `lift` functions. Once the gripper is in the correct position, it performs the appropriate action using the `close`, `insert`, or `lift` functions. 

Note that `check` is a placeholder function that should be replaced with code to check the robot's sensors and determine if the gripper is in the correct position. Additionally, the exact implementation of the `put`, `grab`, `align`, `lift`, `close`, and `insert` functions will depend on the specifics of the robot being used.