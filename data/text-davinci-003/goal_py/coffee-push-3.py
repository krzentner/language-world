
    # Steps:
    #  1. Put gripper near the mug handle
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location
    # First, put the gripper near the mug handle.
    if check("the robot's gripper is not near the mug handle"):
        robot.move_gripper("near the mug handle")
    # If the peg is left of the gripper as seen from in front, we can grab it
    # by moving down.
    if check("the mug is not forward aligned with the robot's gripper and the mug is not left of the robot's gripper"):
        robot.move_gripper("forward aligned with the mug")
    # If the peg is right of the gripper, close the gripper to grab it.
    if check("the mug is left of the robot's gripper and the robot's gripper is open"):
        robot.move_gripper("forward aligned with the mug", close_gripper=True)
    # Once the mug is in the gripper, just move it to the target location.
    if check("the robot's gripper is forward aligned with the mug and the robot's gripper is closed"):
        robot.move_gripper("near the target location")