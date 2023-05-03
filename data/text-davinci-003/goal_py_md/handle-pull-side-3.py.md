

# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab the handle
    #  3. Line the handle up with the slot
    #  4. Pull the handle up from the side
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle becomes right of the gripper, go back to putting the gripper
    # above the handle.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("handle is not right of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    # As long the gripper is still around the handle and the handle isn't lined
    # up with the slot, line up the handle with the slot.
    if check("handle is horizontally aligned with slot"):
        robot.move_gripper("above the handle")
    # If the handle is lined up with the slot to the side, pull it up.
    if check("the robot's gripper is forward aligned with the handle and the handle is not horizontally aligned with slot"):
        robot.move_gripper("horizontally aligned with slot")