# Steps:
    # 1. Move gripper to above the plate
    # 2. Grab plate with the gripper
    # 3. Move gripper to above the target location
    # 4. Align plate with the target location by sliding it back sideways
    # First, put the gripper roughly above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    # Once the gripper is mostly around the plate, we can grab it.
    if check("the robot's gripper is near the plate and the robot's gripper is open"):
        robot.grab("plate")
    # Once we have the plate, we need to move the gripper above the target
    # location.
    if check("the robot's gripper is holding the plate and is not above the target location"):
        robot.place("gripper above target location")
    # To align the plate with the target location, we need to slide it back
    # sideways.
    if check("the robot's gripper is above the target location and the plate is not horizontally aligned with it"):
        robot.slide("plate back sideways into target location")