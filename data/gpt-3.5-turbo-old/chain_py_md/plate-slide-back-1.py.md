# plate-slide-back: slide the plate back into the target location
# def plate_slide_back(robot):
    # Steps:
    # 1. Put the gripper above the plate
    # 2. Drop the gripper around the plate
    # 3. Push the plate back to the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # If the gripper is not around the plate and is open, move it down to pick it up
    if check("the robot's gripper is not around plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # If the gripper is near the plate and the plate is below the gripper, we may have grabbed the plate.
    # Try to slide the plate back to the target location.
    if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
        robot.push("plate back to target location")