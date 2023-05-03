
    # Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper onto plate
    #  3. Push plate to goal
    # To start, we need to put the gripper above the plate.
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.move_gripper("vertically aligned with the plate")
    # Then, move the gripper down onto the plate, trapping it.
    if check("the robot's gripper is vertically aligned with the plate"):
        robot.move_gripper("above the plate", close_gripper=True)
    # If the plate is below the robot's gripper, we can slide it towards the
    # goal.
    if check("the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")