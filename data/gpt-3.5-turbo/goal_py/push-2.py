# Steps:
    #  1. Position the gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location 
    # First, position the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # Once the gripper is above the puck, we can grab it by closing the gripper.
    if check("the robot's gripper is above the puck and the robot's gripper is open"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Once we have the puck in the gripper, move it to the target location.
    if check("the robot's gripper is around the puck and the puck is not at the target location"):
        robot.move_gripper("near the target location")