

Steps:
1. Put the gripper in front of the peg
2. Rotate the gripper to the left to grab the handle of the wrench from the left side
3. Pull the wrench up
4. Put the wrench around the peg carefully
5. Push the end of the wrench back to the peg to ensure it is locked

```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put the gripper in front of the peg
    if check("the robot's gripper is not forward aligned with peg"):
        robot.move_gripper("forward aligned with the peg")
    #  2. Rotate the gripper to the left to grab the handle of the wrench from the left side
    if check("the robot's gripper is not left of the wrench handle"):
        robot.move_gripper("left of the wrench handle", close_gripper=True)
    #  3. Pull the wrench up
    if check("the robot's gripper is horizontally aligned with wrench handle"):
        robot.move_gripper("vertically aligned with the peg")
    #  4. Put the wrench around the peg carefully
    if check("the robot's gripper is vertically aligned with the peg and the wrench is not around the peg"):
        robot.move_gripper("above the peg")
    #  5. Push the end of the wrench back to the peg to ensure it is locked
    if check("the robot's gripper is above the peg and the wrench is around the peg"):
        robot.move_gripper("horizontally aligned with the peg")