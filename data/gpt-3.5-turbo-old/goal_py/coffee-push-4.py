# Steps:
    #  1. Put gripper above the coffee mug
    #  2. Grab the coffee mug with the gripper
    #  3. Move the coffee mug to the target location
    # First, put the gripper above the coffee mug.
    if check("the robot's gripper is not above the coffee mug"):
        robot.move_gripper("above the coffee mug")
    # If the coffee mug is not in the gripper, grab it.
    if check("the robot's gripper is not around the coffee mug and the robot's gripper is open"):
        robot.move_gripper("above the coffee mug", close_gripper=True)
    # Move the coffee mug to the target location.
    if check("the robot's gripper is around the coffee mug and the robot's gripper is not near target location"):
       robot.move_gripper("above the target location")