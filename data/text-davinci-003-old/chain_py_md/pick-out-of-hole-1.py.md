

The steps for this task would be:

1. Put gripper above the hole
2. Drop gripper into the hole
3. Close gripper around peg
4. Lift peg out of the hole
5. Move peg to goal

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Drop gripper into the hole
    #  3. Close gripper around peg
    #  4. Lift peg out of the hole
    #  5. Move peg to goal
    # First, put the gripper above the hole, because it's easier to line up with
    # the peg this way.
    if check("the robot's gripper is not above the hole"):
        robot.put("gripper above hole")
    # If the gripper is below the hole, drop it in and line it up with the peg.
    if check("the robot's gripper is below the hole and the robot's gripper is open"):
        robot.drop("gripper into hole")
    # If the gripper is lined up with the peg, close it and grab the peg.
    if check("the robot's gripper is forward aligned with peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If the gripper is closed around the peg, we can lift it out of the hole.
    if check("the robot's gripper is closed around peg"):
        robot.lift("peg out of hole")
    # Once the peg is out of the hole, move it to the goal.
    if check("the robot's gripper is above the peg"):
        robot.place("peg at goal")
```