# Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to side until near the wall
    #  4. Move gripper around wall
    #  5. Slide puck towards target location
    # First, put the gripper roughly above the puck.
    if check("the robot's gripper is not above puck"):
        robot.move_gripper("above the puck")
    # If the gripper is not around the puck and aligned with it, put it around
    # the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is aligned with the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck, we can start sliding the puck.
    if check("the robot's gripper is near the puck"):
        # Slide the puck to the side until it's near the wall.
        robot.move_gripper("to the side near the wall")
        # Move the gripper around the wall to the other side.
        robot.move_gripper("around the wall")
        # Slide the puck towards the target location.
        robot.move_gripper("above the target location")