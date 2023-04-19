

The program should be:
```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper near handle
    #  2. Grip handle
    #  3. Pull handle up
    # First, put the gripper near the handle, so that we can grab it.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the gripper is near the handle but not gripping it, close the gripper
    # to grab it.
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # Now that the gripper is around the handle, we can pull it up.
    if check("the robot's gripper is closed"):
        robot.move_gripper("above the handle")
 ```