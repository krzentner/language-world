

Then write the program: 

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to the left of the handle
    #  2. Push down on the handle
    # First, put the gripper to the left of the handle.
    if check("the robot's gripper is not to the left of the handle"):
        robot.move_gripper("to the left of the handle")
    # If the gripper isn't aligned with the handle, line it up from the side.
    if check("the robot's gripper is not side-aligned with handle"):
        robot.move_gripper("side-aligned with handle", close_gripper=True)
    # Once the handle is lined up with the gripper, just push down on it.
    if check("the robot's gripper is side-aligned with handle"):
        robot.move_gripper("below the handle")
``