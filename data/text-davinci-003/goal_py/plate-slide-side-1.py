
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into top of plate
    #  3. Slide plate to goal
    # To slide the plate sideway, start by moving the gripper above it.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above plate")
    # If the plate isn't lined up with the gripper as seen from the side, then we
    # should move the gripper left or right to line it up.
    if check("plate is not left of robot's gripper and plate is not right of robot's gripper"):
        robot.move_gripper("side side of the plate")
    # If the plate is left of the gripper but not lined up with the target
    # location, slide the plate to the target location.
    if check("plate is left of robot's gripper"):
        robot.move_gripper("left of the target location")
    # If the plate is right of the gripper but not lined up with the target
    # location, slide the plate to the target location.
    if check("plate is right of robot's gripper"):
        robot.move_gripper("right of the target location")