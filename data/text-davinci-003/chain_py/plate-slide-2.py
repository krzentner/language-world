
    # Steps:
    #  1. Pick up plate handle
    #  2. Move plate to goal
    # First, pick up the plate handle.
    if check("the robot's gripper is not near the plate handle"):
        robot.grab("plate handle")
    # Once the gripper is near the plate handle, start pushing and sliding the
    # plate handle until it's in the desired location.
    if check("the robot's gripper is near the plate handle"):
        robot.move("plate to goal")