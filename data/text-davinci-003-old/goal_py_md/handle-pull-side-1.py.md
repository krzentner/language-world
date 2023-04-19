

The steps for `handle-pull-side` are:
1. Put the gripper near the handle
2. Grab the handle with the gripper
3. Pull the handle up

To complete the program:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper near handle
    #  2. Grab handle with gripper
    #  3. Pull handle up
    # First, move the robot's gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # If the gripper is near the handle, we can try to grab it by moving the
    # gripper around it and closing the gripper.
    if check("the robot's gripper is near the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once we've grabbed the handle, we can pull it up by moving the gripper
    # up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("up")
```