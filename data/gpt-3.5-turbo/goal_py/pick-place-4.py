# Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Move gripper to target location
    #  4. Release puck
    # First, move the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to pick it up.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper has picked up the puck, move it to the target location.
    if check("the robot's gripper is around the puck and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # Once the gripper has reached the target location, release the puck.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location", close_gripper=False)