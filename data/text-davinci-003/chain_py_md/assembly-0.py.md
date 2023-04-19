

This program should do the following: 

1. Put gripper to the left of the peg 
2. Grab the wrench and move it so that it’s aligned with the peg
3. Drop the wrench on the peg 
4. Close the gripper to grasp the wrench and peg 
5. Move the wrench around the peg 

```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper to the left of the peg
    #  2. Grab the wrench and move it so that it's aligned with the peg
    #  3. Drop the wrench on the peg
    #  4. Close the gripper to grasp the wrench and peg
    #  5. Move the wrench around the peg
    if check("the robot's gripper is not to the left of the peg"):
        robot.put("gripper to the left of the peg")
    if check("the robot's gripper is to the left of the peg and the wrench is not forward aligned with the peg"):
        robot.grab("wrench")
        robot.align("wrench with peg")
    if check("the robot's gripper is to the left of the peg and the wrench is forward aligned with the peg and the wrench is not on the peg"):
        robot.drop("wrench onto the peg")
    if check("the robot's gripper is to the left of the peg and the wrench is forward aligned with the peg and the wrench is above the peg"):
        robot.close("gripper around wrench and peg")
    if check("the robot's gripper is to the left of the peg and the wrench is forward aligned with the peg and the wrench is below the peg"):
        robot.move("wrench around the peg")
```