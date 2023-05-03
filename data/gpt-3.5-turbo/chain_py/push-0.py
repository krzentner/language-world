# Steps:
    #  1. Put gripper near the puck
    #  2. Push the puck to the target location
    # If the gripper isn't near the puck, move it to the puck.
    if check("the robot's gripper is not near the puck"):
        robot.move("gripper near the puck")
    # If the gripper is near the puck, push it towards the target location.
    if check("the robot's gripper is near the puck"):
        robot.push("puck to goal")