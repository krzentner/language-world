

The steps for this task are as follows:
1. Put the gripper above the soccer ball
2. Push the gripper down on the soccer ball
3. Slide the soccer ball to the target location

```
# soccer: push the soccer ball into the target location
def soccer(robot):
  # Steps
  #  1. Put the gripper above the soccer ball
  #  2. Push the gripper down on the soccer ball
  #  3. Slide the soccer ball to the target location
  if check("the robot's gripper is not above the soccer ball"):
    robot.move_gripper("above the soccer ball")
  # We should be able to push the ball down by closing the gripper.
  if check("the robot's gripper is above the soccer ball and the robot's gripper is not closed"):
    robot.move_gripper("above the soccer ball", close_gripper=True)
  # Now, if the robot's gripper is still above the soccer ball and closed,
  # it should have a good grip and we can slide the soccer ball to the
  # target location.
  if check("the robot's gripper is above the soccer ball and the robot's gripper is closed"):
    robot.move_gripper("above the target location")
```