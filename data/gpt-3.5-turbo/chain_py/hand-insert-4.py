# Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    # This action is similar to pick-place, but we don't need to be as precise
    # with moving the puck to the target location.
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is not around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.grab("puck")
    # If the gripper is around the puck, move the puck to the target location.
    if check("the robot's gripper is around puck"):
        robot.move("puck to goal")