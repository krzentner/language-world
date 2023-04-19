
    # Steps:
    #  1. Position gripper over the plate
    #  2. Grab the plate with the gripper
    #  3. Slide the plate to target location
    # Move the gripper above the plate before we grab it.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper over the plate")
    # Move the gripper over the plate and close it around it to grab it.
    if check("the robot's gripper is not around the plate and the gripper is open"):
        robot.grab("plate")
    # Move the gripper with the plate to the target location.
    if check("the robot's gripper is around the plate and the plate is not in target position"):
        robot.slide("plate to target location")