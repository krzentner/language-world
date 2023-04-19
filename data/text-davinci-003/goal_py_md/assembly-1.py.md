

Then your code:
```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper 
    #  3. Rotate the tool so the wrench faces the right way 
    #  4. Place the wrench around the peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the peg is not left of the robot's gripper and it is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the peg", close_gripper=True)
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the wrench, rotate the tool so the wrench faces the right way.
    if check("the peg is right of the robot's gripper and the wrench is not aligned with the peg"):
        robot.rotate_tool("aligned with the peg")
    # After putting the wrench around the peg, let go of the peg.
    if check("the wrench is aligned with the peg"):
        robot.move_gripper("above the peg", close_gripper=False)
```