

Steps:
  1. Put gripper left of the handle
  2. Grab the handle with the gripper
  3. Pull the handle up

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper left of the handle
    #  2. Grab the handle with the gripper
    #  3. Pull the handle up
    # Put the gripper left of the handle first.
    if check("the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # If the handle is right of the gripper, grab it.
    if check("the robot's gripper is left of the handle and the handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # Once the handle is grabbed, just pull the handle up.
    if check("the robot's gripper is forward aligned with the handle"):
        robot.move_gripper("up")
``