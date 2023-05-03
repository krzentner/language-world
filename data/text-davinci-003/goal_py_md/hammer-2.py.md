

The robot must perform the following steps to complete the task:

1. Move the gripper near the hammer handle.
2. Close the gripper around the hammer handle.
3. Move the hammer to the nail.
4. Lower the hammer and hit the nail.

```
# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Move gripper near hammer handle
    #  2. Close gripper around hammer handle
    #  3. Move hammer to nail
    #  4. Lower hammer and hit nail
    # First, move the gripper near the hammer handle.
    if check("the robot's gripper is not near the hammer handle"):
        robot.move_gripper("near the hammer handle")
    # If the gripper isn't around the hammer handle, close it around it.
    if check("the robot's gripper is not around hammer handle and the robot's gripper is open"):
        robot.move_gripper("around the hammer handle", close_gripper=True)
    # If the gripper is around the hammer and the hammer isn't near the nail,
    # move the hammer near the nail.
    if check("the robot's gripper is around hammer handle and the hammer is not near the nail"):
        robot.move_gripper("near the nail")
    # If the hammer is near the nail, lower the hammer to hit the nail.
    if check("the robot's gripper is near the nail"):
        robot.move_gripper("below the nail")
``