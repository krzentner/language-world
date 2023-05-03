# Steps:
    #  1. Put gripper above plate
    #  2. Drop gripper around plate's edge
    #  3. Push the plate towards target location
    # The robot can slide the plate by trapping it by pushing down on it from
    # above its edge and moving the gripper.
    # First put the gripper roughly above the plate, so it doesn't bump into it.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the plate isn't in the gripper yet, put the gripper around its edge.
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.move_gripper("around the plate", close_gripper=True)
    # Once the gripper is around the plate, push it towards the target location.
    if check("the robot's gripper is around the plate and the plate is below the robot's gripper"):
        robot.move_gripper("near the target location")