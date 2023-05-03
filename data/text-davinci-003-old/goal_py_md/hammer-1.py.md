

The steps for this task are: 
1. Put the gripper above the hammer handle
2. Drop the gripper around the hammer handle
3. Close the gripper around the hammer handle
4. Swing the hammer to hit the nail

```
# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put gripper above hammer handle
    #  2. Drop gripper around hammer handle
    #  3. Close gripper around hammer handle
    #  4. Swing hammer to hit nail 
    # First, put the gripper roughly above the hammer handle, so that we don't
    # bump it while trying to grab it.
    if check("the robot's gripper is not above the hammer handle"):
        robot.move_gripper("above the hammer handle")
    # Once the gripper is above the hammer handle, we should be able to grab it
    # by moving the gripper down around it.
    if check("the robot's gripper is above the hammer handle and the robot's gripper is not around the hammer handle"):
        robot.move_gripper("around the hammer handle", close_gripper=True)
    # Once the gripper is around the hammer handle, we can start swinging it to
    # hit the nail.
    if check("the robot's gripper is around the hammer handle"):
        robot.move_gripper("forward of the nail")
    # Once the gripper is in front of the nail, swing the hammer downwards to
    # hit the nail.
    if check("the robot's gripper is forward the nail"):
        robot.move_gripper("above the nail")