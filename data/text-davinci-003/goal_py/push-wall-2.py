
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck around the wall
    # We can first try to slide the puck around the wall by pushing the puck from
    # the side.
    # We first need to make sure the gripper is aligned with the puck from the
    # side.
    if check("the robot's gripper is not sideways aligned with the puck"):
        robot.move_gripper("sideways aligned with the puck", close_gripper=True)
    # Now that the gripper is lined up, just push the puck around the wall.
    if check("the robot's gripper is sideways aligned with the puck and the robot's gripper is not near the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and gripping it, we can just slide it 
    # around the wall to the target location.
    if check("the robot's gripper is near the puck and the robot's gripper is gripping the puck"):
        robot.move_gripper("around the wall")