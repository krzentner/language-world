
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Move the gripper above the target location
    #  4. Drop the puck at the target location
    # To pick up an object, we need to move the gripper above it and then drop
    # it around it.
    # If the puck isn't directly below the gripper, move the gripper above the
    # puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # As long as the gripper is aligned with the puck, closing it should move it
    # around the puck.
    if check("the robot's gripper is above the puck"):
        robot.move_gripper("vertically aligned with the puck", close_gripper=True)
    # Now the gripper is around the puck, so we can move it to the target
    # location.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("above the target location")
    # Once the gripper is above the target location, we can let go of the puck.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("around the target location")