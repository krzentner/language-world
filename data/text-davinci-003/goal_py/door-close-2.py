
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push closed the door
    # First, put the gripper roughly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("right of the door handle", close_gripper=True)
    # If the gripper is around the door handle, we can push the door closed.
    if check("the robot's gripper is around door handle and the robot's gripper is not around the door handle at target position"):
        robot.move_gripper("around the door handle at the target position")