
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Push the puck towards the target
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the puck becomes left of the gripper, go back to putting the gripper
    # above the puck.
    # Because the puck is a small object, we check if the gripper is around it
    # instead of only forward aligned.
    if check("puck is not left of the robot's gripper and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck")
    # As long as the puck is still near the gripper, push the puck towards the
    # target.
    if check("the robot's gripper is forward aligned with puck and the robot's gripper is around the puck"):
        robot.move_gripper("left of the target")