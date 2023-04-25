

Steps:
1. Put gripper to the left of the handle
2. Grab the handle with the gripper
3. Push the handle down

```
# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper to the left of the handle
    #  2. Grab the handle with the gripper
    #  3. Push the handle down
    # First, put the gripper to the left of the handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # Once the gripper is left of the handle, we can grab it by moving the
    # gripper around it and closing the gripper.
    if check("the robot's gripper is left of the handle and the robot's gripper is open"):
        robot.move_gripper("around the handle", close_gripper=True)
    # Once the gripper is around the handle, we can just push the handle down.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("horizontally aligned with the handle")
```