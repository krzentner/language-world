# Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    #  4. Release the puck at the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is not around the puck, move it down to grab it.
    if check("the robot's gripper is not around the puck and the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once the gripper is around the puck, move the puck to the target location.
    if check("the robot's gripper is holding the puck and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Once the puck is at the target location, release it.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("above the puck", open_gripper=True)