Here's the code to perform the `pick-out-of-hole` task:

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move("gripper above hole")
    if check("the gripper is not around peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    if check("the gripper is near peg and the robot's gripper is open"):
        robot.grab("peg")
    if check("the gripper is around peg and peg is out of the hole"):
        robot.place("peg at goal")
``` 

The `pick_out_of_hole` task first moves the gripper to be above the hole. It then checks if the gripper is not already around the peg and the gripper is open. If this condition is true, it drops the gripper around the peg. Then, it checks if the gripper is near the peg and the gripper is open. If this condition is true, it grabs the peg. Finally, it checks if the gripper is around the peg and the peg is out of the hole. If this condition is true, it places the peg at the goal location.