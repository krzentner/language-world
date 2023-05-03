

The program for the `assembly` task would look like this:

```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put the gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Put the wrench around the peg
    #  4. Move the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench becomes left of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("wrench is not left of the robot's gripper and wrench is not aligned with the robot's gripper forward"):
        robot.grab("wrench")
    # As long the gripper is still mostly around the wrench and the wrench isn't
    # lined up with the peg, line up the wrench with the peg.
    if check("the robot's gripper is aligned with the wrench forward and the wrench is not in line with the peg"):
        robot.align("wrench to peg")
    # If the peg is lined up with the wrench from the side, move the wrench
    # around the peg.
    if check("wrench is in line with the peg"):
        robot.move("wrench around peg")
```