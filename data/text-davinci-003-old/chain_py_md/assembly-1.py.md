

Steps:
1. Put the gripper above the peg
2. Drop the gripper around the peg 
3. Move the gripper to the wrench
4. Put the wrench around the peg
5. Close the gripper around the wrench and peg

```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put the gripper above the peg
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    #  2. Drop the gripper around the peg
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    #  3. Move the gripper to the wrench
    if check("the robot's gripper is not near the wrench"):
        robot.move("gripper to the wrench")
    #  4. Put the wrench around the peg
    if check("the wrench is not around the peg"):
        robot.put("wrench around peg")
    #  5. Close the gripper around the wrench and peg
    if check("the robot's gripper is not closed around the wrench and peg"):
        robot.close("gripper around wrench and peg")
```