
    # Steps:
    #  1. Push puck against wall
    #  2. Slide puck to goal
    # If the robot's gripper isn't in front of the puck, move the gripper to the
    # puck.
    if check("the robot's gripper is forward aligned with the puck"):
        robot.move_gripper("near the wall")
    # If the gripper is in front of the puck, push the puck against the wall.
    if check("the robot's gripper is near the wall and the puck is not near the wall"):
        robot.move_gripper("forward aligned with the target location")
    # If the puck is near the wall and the gripper is opposite the goal, slide
    # the puck sideways towards the goal.
    if check("the robot's gripper is forward aligned with the target location and the puck is near the wall"):
        robot.move_gripper("forward aligned with the puck")