# Steps:
    #  1. Move gripper towards the wall
    #  2. Slide gripper over the wall
    #  3. Move gripper to the target location
    # Since there is a wall in the way, we need to first move the gripper towards
    # the wall but not too close that it can't slide over it.
    if check("the robot's gripper is not positioned near the wall"):
        robot.move("gripper towards the wall")
    # If the gripper is near the wall, we need to slide it over the wall in order
    # to reach the target location. We need to check if the gripper is in front
    # of the wall and not below or about to hit it.
    if check("the robot's gripper is in front of the wall and gripper is not below the top of the wall and gripper is not touching the wall"):
        robot.slide("gripper over the wall")
    # Once the gripper is over the wall, we can move it to the target location.
    if check("the robot's gripper is over the wall and not at the target location"):
        robot.reach("to goal")