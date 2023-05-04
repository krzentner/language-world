

To perform a task, the robot has to start by holding an object that is `above the table`.
If the object isn't `above the table`, the robot will place it on the table.

When you're done writing code, evaluate:

```
robot.task(disassemble)
```

to see what the task you coded looks like.
""")
 
instructions['disassemble'] = """```
# disassemble: pull the wrench off the peg
def disassemble(robot):
    # Steps:
    #  1. Put gripper above wrench
    #  2. Drop gripper around wrench
    #  3. Pull wrench off peg
    # We need to put the gripper above the wrench before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not almost vertically aligned with wrench"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    # Once the gripper is lined up above the wrench, we should be able to
    # grab the wrench by moving the gripper down around it.
    if check("the robot's gripper is around wrench"):
        robot.move_gripper("around the wrench", close_gripper=True)
    # Once the gripper is around the wrench, we can just pull the wrench off
    # the peg.
    if check("the robot's gripper is below wrench"):
        robot.move_gripper("below the wrench")

# pick-out-of-hole: pick the peg out of the hole
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Lift peg out of hole
    # First, put the gripper roughly above peg, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above peg"):
        robot.move_gripper("above peg", close_gripper=True)
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is above peg and the robot's gripper is not around peg"):
        robot.move