

Solution:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above peg
    #  2. Flip the peg to the side
    #  3. Drop gripper around peg
    #  4. Push peg into hole
    #  5. Release peg in the hole
    # Start by moving the robot's gripper above the peg.
    if check("the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    # If the peg is positioned correctly and the gripper is above it, try flipping
    # it to the side.
    if check("the robot's gripper is above the peg and the peg is upright"):
        robot.flip("peg to the side")
    # Now that the peg is sideways, we can try dropping the gripper around it.
    if check("the robot's gripper is above the peg and the peg is to the side"):
        robot.drop("gripper around peg")
    # If the gripper is around the peg, push the peg into the hole.
    if check("the robot's gripper is around the peg"):
        robot.push("peg into the hole")
    # Now that the peg is in the hole, we should release the gripper so the peg
    # stays put.
    if check("the robot's gripper is still around the peg and the peg is in the hole"):
        robot.release("gripper around peg")
```