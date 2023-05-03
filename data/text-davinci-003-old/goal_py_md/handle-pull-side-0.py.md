

Steps:
1. Place the gripper left of the handle 
2. Wrap the gripper around the handle
3. Pull the handle up

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Place the gripper left of the handle 
    #  2. Wrap the gripper around the handle
    #  3. Pull the handle up
    # To pull the handle up from the side, the gripper needs to be left of the
    # handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # If the gripper is in the correct position, wrap it around the handle and
    # make sure it's closed.
    if check("the robot's gripper is left of the handle and the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If the robot's gripper is around the handle and closed, pull up the handle.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("left of the handle")