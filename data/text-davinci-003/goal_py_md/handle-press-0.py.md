

Steps:
1. Put gripper above handle
2. Drop gripper around handle
3. Close gripper around handle 
4. Push down on handle

```
# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Close gripper around handle
    #  4. Push down on handle
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # If the gripper is near the handle and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above handle and the robot's gripper is closed"):
        robot.move_gripper("near the handle", close_gripper=True)
    # Once the handle is trapped by the robot's gripper, we can move the
    # gripper downwards and push the handle down.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("below the handle")