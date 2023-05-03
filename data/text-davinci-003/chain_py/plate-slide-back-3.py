
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Push gripper into front of plate
    #  3. Slide plate back to goal
    # The robot can slide the plate by trapping it with the gripper.
    # Start by moving the gripper in front of the plate.
    if check("the robot's gripper is not forward aligned with plate"):
        robot.put("gripper in front of plate")
    # If the gripper is forward aligned with the plate, close the gripper to trap
    # the plate.
    if check("the robot's gripper is forward aligned with plate and the robot's gripper is not around plate"):
        robot.close("gripper around plate")
    # Once the plate is trapped and the gripper is closed, slide the plate.
    if check("the robot's gripper is around plate"):
        robot.slide("plate back to goal")