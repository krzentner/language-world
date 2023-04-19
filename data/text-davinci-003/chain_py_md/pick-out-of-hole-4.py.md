

The program should perform the following steps:

1. Put gripper above the hole
2. Drop gripper around the peg
3. Grab the peg with the gripper
4. Move the peg to the target location

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Drop gripper around the peg
    #  3. Grab the peg with the gripper
    #  4. Move the peg to the target location
    # First, put the gripper above the hole.
    if check("the robot's gripper is not above the hole"):
        robot.put("gripper above hole")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # If the gripper is near the peg and open, grab the peg by closing the 
    # gripper.
    if check("the robot's gripper is near the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper, and the peg is still near the gripper, so we've 
    # probably grabbed it.
    # Try to move the peg to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.place("peg at target location")
```