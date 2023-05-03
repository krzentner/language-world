# Steps:
    #  1. Move the gripper to the target location
    # We don't need to grab anything for a reach action, we just need to move the
    # gripper to the target location.
    # Move the gripper to the goal.
    if check("the robot's gripper is not at the goal location"):
        robot.move("gripper to goal location")