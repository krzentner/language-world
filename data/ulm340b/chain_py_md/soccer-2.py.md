

Then, use the instructions you see in the other program blocks to describe the
following steps:

  1. Put the gripper above the soccer ball.
  2. Slide the gripper above the soccer ball.
  3. Slide the gripper to the target.
  4. Push the soccer ball to the target by sliding the gripper.
  5. Push harder to move the soccer ball all the way to the target.

Here are some instructions that might help:

```
# Some helpful instructions.
if check("the soccer ball is not below robot's gripper and the robot's gripper is not near the soccer ball"):
    robot.put("the gripper above the soccer ball")
if check("the soccer ball is below robot's gripper and the robot's gripper is not near the soccer ball"):
    robot.push("the gripper into the soccer ball")
if check("the soccer ball is below robot's gripper and the robot's gripper is near the soccer ball"):
    robot.slide("the soccer ball to the goal")
```

For each line, fill in the appropriate instruction to complete the task.

Once you think you have the correct program, you can test it out to see if it works by typing `run soccer()`.

Your code should look like:
```
# soccer: push the soccer ball into the target location
def soccer(robot):
    # Steps:
    #  1. Put the gripper above the soccer ball.
    #  2. Slide the gripper above the soccer ball.
    #  3. Slide the gripper to the target.
    #  4. Push the soccer ball to the target by sliding the gripper.
    #  5. Push harder to move the soccer ball all the way to the target.
    if check("the soccer ball is not below robot's gripper and the robot's gripper is not near the soccer ball"):
        robot.put("the gripper above the soccer ball")
    if check("the soccer ball is below robot's gripper and the robot's gripper is not near the soccer ball"):
        robot.push("the gripper into the soccer ball")
    if check("the soccer ball is below robot's gripper and the robot's gripper is near the soccer ball"):
        robot.slide("the soccer ball to the goal")
    if check("the soccer ball is near the robot's gripper"):
        robot.slide("the soccer ball to the