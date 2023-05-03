# Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move gripper to target location
    #  4. Release the puck
    # We need to put the gripper above the puck before we can grab it.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # Once the gripper is above the puck, we can grab it.
    if check("the robot's gripper is above the puck and the robot's gripper is open"):
        robot.grab("puck")
    # Once we have the puck, we need to move the gripper to the target location
    # by sliding it.
    if check("the robot is holding the puck and the robot's gripper is not at the target location"):
        robot.slide("gripper to target location")
    # At the target location, we can release the puck.
    if check("the robot's gripper is at the target location and the robot is holding a puck"):
        robot.release("puck")