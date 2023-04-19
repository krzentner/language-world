

Then add the following steps:

1. Put gripper above the peg
2. Grab the peg with the gripper
3. Line the wrench up with the peg
4. Move the wrench around the peg

```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the wrench up with the peg
    #  4. Move the wrench around the peg
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the wrench isn't lined
    # up with the peg, line up the wrench with the peg.
    if check("the robot's gripper is forward aligned with the peg and the wrench is not horizontally aligned with peg"):
        robot.align("wrench to peg")
    # If the wrench is lined up with the peg to the side, move it around the peg.
    if check("wrench is horizontally aligned with peg"):
        robot.move("wrench around peg")
```