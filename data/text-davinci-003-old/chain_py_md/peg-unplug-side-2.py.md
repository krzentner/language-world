

And finish with:

```
# If the robot's gripper is still around the peg and the peg is lined up with
# the hole to the side, pull it out.
if check("the robot's gripper is around peg and peg is horizontally aligned with hole"):
    robot.pull("peg out from hole")
```