# Steps:
    #  1. Put gripper above plate
    #  2. Lower gripper onto plate
    #  3. Push plate towards target location
    # We need to line up the gripper with the plate first.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate, we can lower it onto the plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not touching the plate"):
        robot.move_gripper("on top of the plate", close_gripper=True)
    # Once the gripper has grabbed the plate, we can slide it to the target
    # location.
    if check("the robot's gripper is holding the plate and the plate is below the robot's gripper"):
        robot.move_gripper("above the target location")