
    # Steps:
    #  1. Put gripper above the dial
    #  2. Lower gripper onto the dial
    #  3. Push the dial to the right
    # If the dial isn't above the gripper as seen from the top, move the gripper
    # near the dial.
    if check("the dial is right of the robot's gripper and the robot's gripper is below the dial"):
        robot.move("gripper to left of dial")
    # If the gripper is near the dial and the dial is above the gripper as seen
    # from the top, we probably have the dial lined up, so try pushing the dial
    # to the right.
    if check("the robot's gripper is near the dial and dial is above the robot's gripper"):
        robot.push("dial to the right")