# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with gripper
    #  3. Move the plate to the target location
    # We need to start by putting the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # Once the gripper is above the plate, we should be able to grab the plate
    # by moving the gripper down around it.
    if check("the robot's gripper is above the plate and the gripper is not around the plate"):
        robot.drop("gripper around plate")
    # Once the gripper is around the plate, we can just slide the plate to the
    # target location.
    if check("the robot's gripper is around the plate"):
        robot.slide("plate to the goal")