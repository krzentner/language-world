

Answer:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper to side of peg
    #  2. Drop gripper around peg
    #  3. Pick up peg
    #  4. Insert peg into the hole from the side
    # First, we need to move the gripper to the side of the peg, so that we can
    # grab it by going around.
    if check("the robot's gripper is not near the side of the peg"):
        robot.place("gripper to side of peg")
    # If the gripper is close to the side of the peg, we can go around and
    # grab it.
    if check("the robot's gripper is near the side of the peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # Once we have grabbed the peg, the robot can pick up the peg.
    if check("the robot's gripper is around peg and the robot's gripper is closed"):
        robot.lift("peg")
    # Now that we have the peg in the robot's grip, we can insert the peg into
    # the hole from the side.
    if check("the robot's gripper is holding peg"):
        robot.put("peg in hole from side")
```