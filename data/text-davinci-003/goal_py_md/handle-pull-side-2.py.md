

Steps:
  1. Put gripper next to handle
  2. Grab handle with gripper
  3. Pull handle up

If the gripper is not near the handle, move the gripper next to the handle.
```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper next to handle
    #  2. Grab handle with gripper
    #  3. Pull handle up
    # If the gripper is not near the handle, move the gripper next to the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle", close_gripper=True)

    # If the gripper is near the handle, grab it by closing the gripper.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("left of the handle")

    # If the gripper is now left of the handle, pull it up.
    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("above the handle")