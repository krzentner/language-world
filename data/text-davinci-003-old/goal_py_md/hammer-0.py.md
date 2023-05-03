

Steps:
1. Put gripper above the hammer handle
2. Drop gripper around hammer handle
3. Put gripper above the nail 
4. Swing the hammer to hit the nail

If the robot's gripper is not vertically aligned with the hammer handle, we should move the gripper near the hammer handle to start swinging it.

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above the hammer handle
    #  2. Drop gripper around hammer handle
    #  3. Put gripper above the nail 
    #  4. Swing the hammer to hit the nail
    # If the robot's gripper is not vertically aligned with the hammer handle, we should move the gripper near the hammer handle to start swinging it.
    if check("the robot's gripper is not vertically aligned with the hammer handle"):
        robot.move_gripper("vertically aligned with the hammer handle", close_gripper=True)
    # If the gripper is horizontally aligned with the hammer handle and the nail is left of the gripper, we should move the gripper around the nail before we swing.
    if check("the robot's gripper is horizontally aligned with the hammer handle and the nail is left of the robot's gripper"):
        robot.move_gripper("left of the nail")
    # If the gripper is located above or around the nail, we should swing the hammer.
    if check("the robot's gripper is above the nail or the robot's gripper is around the nail"):
        robot.move_gripper("vertically aligned with the nail")
    # Once the gripper is in the right position, hit the nail with the hammer.
    if check("the robot's gripper is vertically aligned with the nail and the gripper has something to grip"):
        robot.move_gripper("away from the nail")