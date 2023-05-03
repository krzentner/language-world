# Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    #  4. Release the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # Once we're above the puck, we can grab it with the gripper.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not closed around the puck"):
        robot.grab("puck")
    # Once we have the puck, we can move it to the target location.
    if check("the robot's gripper is closed around the puck and the robot's gripper is not above the target location"):
        robot.move("puck to target")
    # Once we're at the target location, we can release the puck.
    if check("the puck is at the target location and the robot's gripper is closed around the puck"):
        robot.release("puck")