# Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the gripper to the target location
    #  4. Place the puck down at the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is not around the puck, grab the puck.
    if check("the robot's gripper is not around the puck"):
        robot.grab("puck")
    # Move the gripper to the target location.
    if check("the robot's gripper is holding the puck and is not at the target location"):
        robot.move("gripper to goal location")
    # Place the puck down at the target location.
    if check("the robot's gripper is holding the puck and is at the target location"):
        robot.put_down("puck")