
    # Steps:
    #  1. Put gripper between the puck and wall
    #  2. Push gripper into the side of the puck
    #  3. Slide the puck to the goal
    # We'll need to trap the puck to slide it, but because of the small wall
    # blocking the way we'll need to grab it from the side.
    if check("the robot's gripper is between puck and wall"):
        robot.move_gripper("left of the puck")
    # If the gripper is between the puck and the wall, but not touching the puck,
    # we can grab it by closing the gripper.
    # Close the gripper to make sure we have control over the puck.
    if check("the robot's gripper is between puck and wall and the robot's gripper is partially closed"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is trapping the puck, slide it to the goal.
    if check("the robot's gripper is trapping the puck against the wall"):
        robot.move_gripper("above the target location")