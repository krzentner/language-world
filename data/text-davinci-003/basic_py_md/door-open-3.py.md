

Then, complete the function to make the robot successfully open the door:

```
# door-open: pull the door open
def door_open(robot):
  if check("the robot's gripper is not above the door handle"):
      robot.place("gripper above door handle")
  if check("the robot's gripper is not around the door handle"):
      robot.grab("door handle")
  if check("the robot's gripper is around the door handle"):
      robot.pull("handle open")