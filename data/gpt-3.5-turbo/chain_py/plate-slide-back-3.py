# Steps:
    #  1. Put gripper under the plate
    #  2. Slide the gripper with the plate back to the target location
    # First, put the gripper under the plate
    if check("the robot's gripper is not under the plate"):
        robot.put("the gripper under the plate")
    # If the gripper is under the plate, slide the gripper with the plate back
    # to the target location.
    if check("the robot's gripper is under the plate"):
        robot.slide("the plate back to the target location")