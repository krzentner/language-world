# Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate
    #  3. Push the plate back into the target location
    # Put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("the gripper above the plate")
    # Once the gripper is lined up above the plate, grab the plate by moving
    # the gripper down around it.
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate"):
        robot.drop("the gripper around the plate")
    # If the gripper is around the plate, push it back into the target location.
    if check("the robot's gripper is around the plate"):
        robot.push("the plate back into the target location")