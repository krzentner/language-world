



```python
def shelf_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper above block
    if check("the robot's gripper is not above block"):
        robot.move_gripper("above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.move_gripper("near block", close_gripper=True)
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
```

### Part 3

Finally, we'll work on the task that started all of this: picking up and holding the remote. Here are some examples that help explain how the robot's gripper works:

```
robot.gripper_position()
#=> (3.0, 4.0, 0.0, 0.0)
robot.grip_force()
#=> -3.45
# Note: The robot automatically grips down when we move the gripper.
robot.move_gripper("vertically aligned with remote")
robot.grip_force()
#=> -3.45
# Note: The robot automatically grips down when we move the gripper.
robot.move_gripper("around remote")
robot.grip_force()
#=> -3.03
# Note: The robot automatically grips down when we move the gripper.
robot.move_gripper("near remote")
robot.grip_force()
#=> -1.07
# Note: We can tell the robot to grip harder.
robot.grip_force()
#=> -3.03
# Note: We can tell the robot to grip harder.
robot.grip_force()
#=> -0.54
# Note: We can tell the robot to grip harder.
robot.grip_force()
#=> -3.24
# Note: If we tell the robot to open the gripper, it will move to open.
robot.move_gripper