# Steps:
    #  1. Put gripper left of the plate
    #  2. Slide gripper under the plate
    #  3. Move gripper right to slide the plate back
    # Because the plate needs to be slid back sideways, we need to move the
    # gripper under the plate. First, move the gripper to the left of the plate.
    if check("the robot's gripper is not left of the plate"):
        robot.move("gripper to left of the plate")
    # Once the gripper is to the left of the plate, move it under the plate.
    if check("the robot's gripper is not underneath the plate"):
        robot.slide("gripper under the plate")
    # Once the gripper is under the plate, we can slide the plate back by moving
    # the gripper to the right.
    if check("the robot's gripper is under the plate and the robot's gripper is not right of the plate"):
        robot.slide("the plate back by moving the gripper right")