
    # Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate with the gripper
    #  3. Push the plate into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # If the plate is not being held by the gripper, grab it by closing around
    # it.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.grab("plate")
    # Once the gripper is around the plate, push the plate into the target
    # location.
    if check("the robot's gripper is around the plate"):
        robot.push("plate into target location")