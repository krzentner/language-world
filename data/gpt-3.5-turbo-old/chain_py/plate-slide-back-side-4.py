# Steps:
    #  1. Put gripper above plate
    #  2. Grab the plate from the top
    #  3. Move the gripper back
    #  4. Slide the plate sideways into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # Once the gripper is above the plate, grab it from the top.
    if check("the robot's gripper is above the plate and the gripper is open"):
        robot.grab("plate from top")
    # Now that we have the plate, move the gripper back.
    if check("the plate is inside the gripper"):
        robot.move("gripper back")
    # Slide the plate sideways into the target location.
    if check("the robot's gripper is near the target location and the plate is inside the gripper"):
        robot.slide("plate sideways into target location")