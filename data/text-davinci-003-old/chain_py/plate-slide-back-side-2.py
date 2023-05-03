
    # Steps:
    #  1. Put gripper left of plate
    #  2. Slide plate to the right
    #  3. Put plate into target location
    # If the gripper is not near the plate, it should move towards the plate.
    if check("the robot's gripper is not near the plate"):
        robot.put("gripper left of the plate")
    # If the robot's gripper is lined up with the plate, it should push it
    # back.
    if check("the robot's gripper is horizontally aligned with the plate"):
        robot.slide("plate to the right")
    # When the gripper has moved the plate to the target location, it should
    # hold it there.
    if check("the robot's gripper is at the target location and the plate is left of the robot's gripper"):
        robot.place("plate in target location")