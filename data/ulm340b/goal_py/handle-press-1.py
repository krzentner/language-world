
    # Steps:
    #  1. Put gripper right of handle
    #  2. Close gripper on handle
    #  3. Push down on handle
    # First, put the gripper roughly right of the handle.
    # Because the handle is tall, we don't have to be very precise.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once we are lined up with the handle, we can close the gripper on the
    # handle.
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.move_gripper("above the handle", close_gripper=True)
    # If the handle is above the gripper, we can push it down.
    # We can close the gripper to make sure we are holding onto the handle as we
    # press it down.
    if check("the robot's gripper is above the handle and the robot's gripper is closed"):
        robot.move_gripper("left of the handle", close_gripper=True)

# handle-pull: pull the handle up
def handle_pull(robot):
    # Steps:
    #  1. Put gripper left of handle
    #  2. Close gripper on handle
    #  3. Pull up on handle
    # First, put the gripper roughly left of the handle.
    # Because the handle is tall, we don't have to be very precise.
    if check("the robot's gripper is not near the handle"):
        robot.move_gripper("near the handle")
    # Once we are lined up with the handle, we can close the gripper on the
    # handle.
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.move_gripper("above the handle", close_gripper=True)
    # If the handle is above the gripper, we can pull it up.
    # We can close the gripper to make sure we are holding onto the handle as we
    # pull it up.
    if check("the robot's gripper is above the handle and the robot's gripper is closed"):
        robot.move_gripper