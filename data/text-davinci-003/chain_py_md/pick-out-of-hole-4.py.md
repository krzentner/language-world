

Then, write steps for the robot to complete:

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above hole
    #  2. Drop gripper around hole
    #  3. Close gripper around peg
    #  4. Lift peg out of hole
    #  5. Move peg to goal
    # First, put the gripper above the hole so that we don't bump the peg while
    # trying to grab it.
    if check("the robot's gripper is not above the hole"):
        robot.place("gripper above hole")
    # If the grip is not around the hole, put it around it.
    if check("the robot's gripper is not around hole and the robot's gripper is open"):
        robot.drop("gripper around hole")
    # If the gripper is around the hole, close it around the peg.
    if check("the robot's gripper is around the hole and the robot's gripper is open"):
        robot.close("gripper around peg")
    # If the gripper is closed around the peg, lift the peg out of the hole.
    if check("the robot's gripper is closed around the peg and the peg is still in the hole"):
        robot.lift("peg out of hole")
    # If the peg is out of the hole, move it to the target location.
    if check("the peg is out of the hole"):
        robot.place("peg at goal")
```