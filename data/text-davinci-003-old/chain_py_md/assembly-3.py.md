

Here's the program:
```
# assembly: put the wrench around the peg
# def assembly(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Grab wrench with gripper
    #  3. Line up wrench with peg
    #  4. Drop wrench around peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # Once the gripper is above the wrench, grab it.
    if check("the robot's gripper is vertically aligned with wrench and the robot's gripper is open"):
        robot.grab("wrench")
    # Align wrench with peg
    if check("the robot's gripper is above peg and wrench is not horizontally aligned with peg"):
        robot.align("wrench to peg")
    # Drop wrench around peg.
    if check("the robot's gripper is horizontally aligned with peg and the robot's gripper is open"):
        robot.drop("wrench around peg")
```