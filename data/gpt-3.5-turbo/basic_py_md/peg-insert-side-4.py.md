Here's the code to perform the `peg-insert-side` task:

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not near the peg"):
        robot.reach("to the peg")
    if check("the robot's gripper is near the peg and the robot's gripper is not around the peg"):
        robot.put("gripper around the peg")
    if check("the robot's gripper is around the peg and the peg is not near the hole"):
        robot.move("gripper to the side of the hole")
    if check("the robot's gripper is next to the hole and the robot's gripper is not in front of the hole"):
        robot.move("gripper towards the hole")
    if check("the robot's gripper is in front of the hole and the robot's gripper is not above the hole"):
        robot.move("gripper up to the hole")
    if check("the robot's gripper is above the hole and the robot's gripper is closed"):
        robot.drop("peg into the hole")
``` 

This code first checks if the robot's gripper is near the peg, and then puts the gripper around the peg if not. It then moves the gripper to the side of the hole and pushes it towards the hole. Finally, it drops the peg into the hole when the gripper is above the hole and the gripper is closed.