
    # Steps:
    #  1. Put gripper above plate
    #  2. Push plate sideways
    #  3. Slide plate to goal
    # Put the gripper above the plate to start pushing it.
    if check("the robot's gripper is not above plate"):
        robot.go("gripper to above plate")
    # Push the plate to the left or right to start sliding it.
    if check("the robot's gripper is above plate and the plate is not left of the robot's gripper or right of the robot's gripper"):
        robot.push("plate left")
    # Start sliding the plate.
    if check("plate is left of robot's gripper or right of robot's gripper"):
        robot.slide("plate to goal")