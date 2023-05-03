
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Line up puck with target
    #  4. Place puck at target
    # Put the gripper above the puck
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck", close_gripper=True)
    # Close the gripper to grab the puck
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.move_gripper("above the target location")
    # Once the puck is lined up with the target, drop it.
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("below the target location")