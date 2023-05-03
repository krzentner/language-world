# Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper to the target location
    #  4. Release the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is above the puck, move the gripper down to grab the puck.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # If the gripper has the puck, move it to the target location.
    if check("the robot's gripper is around the puck and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")
    # If the gripper is at the target location, release the puck.
    if check("the robot's gripper is near the target location and the gripper is holding onto something"):
        robot.move_gripper("at the target location", close_gripper=False)