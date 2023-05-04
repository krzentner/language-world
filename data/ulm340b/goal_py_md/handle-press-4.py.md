

The functions you will use in the program are:

- `check`. This function takes in a string describing a constraint that should
  be true, such as "the robot's gripper is above the puck". It returns `False`
  if the constraint is not true, and `True` otherwise.

- `robot.move_gripper`. This function takes in a string describing how the
  robot should move its gripper, and tries to perform that action. For example,
  "above the puck" means the robot will try to put the gripper above the puck.
  `robot.move_gripper` does not return anything.

"""

# Handle-press-code

# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # If the gripper is around the handle and the handle is not in front of the gripper,
    # put the gripper down to push on the handle.
    if check("the robot's gripper is forward aligned with the handle and the robot's gripper is not near the handle"):
        robot.move_gripper("above the handle", close_gripper=True)
    # If the gripper is below the handle, we've probably trapped the handle and can
    # slide it to the push.
    # Close the gripper to make sure we keep control of the handle.
    if check("the robot's gripper is near the handle and the handle is below the robot's gripper"):
        robot.move_gripper("vertically aligned with handle")


def check(