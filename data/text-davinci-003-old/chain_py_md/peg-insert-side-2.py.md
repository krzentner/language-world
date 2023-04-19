

The program should be:

```
# peg-insert-side: insert the peg into the hole from the side
# def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper roughly above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # Once the gripper is lined up above the peg, we should be able to grab the
    # peg by closing the gripper.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # Once the gripper is around the peg, we can line up the peg with the hole.
    if check("the robot's gripper is around peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")
```