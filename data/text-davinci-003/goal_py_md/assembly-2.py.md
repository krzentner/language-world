

Then add the following lines to complete the script:

```
    # Steps:
    #  1. Put gripper just above the wrench
    #  2. Put gripper below the peg
    #  3. Grab the peg with the gripper
    #  4. Put the wrench around the peg
    # Put the gripper just above the wrench.
    if check("the robot's gripper is not above the wrench"):
        robot.move_gripper("above the wrench")
    # Put the gripper below the peg.
    if check("the robot's gripper is above the wrench and the robot's gripper is not below the peg"):
        robot.move_gripper("below the peg")
    # Grab the peg with the gripper.
    if check("the robot's gripper is below the peg and the robot's gripper is not around the peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    # Put the wrench around the peg.
    if check("the robot's gripper is around the peg"):
        robot.move_gripper("around the peg")
```