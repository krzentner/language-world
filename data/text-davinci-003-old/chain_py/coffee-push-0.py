
    # Steps:
    #  1. Put gripper above mug
    #  2. Grab mug with gripper
    #  3. Move mug to target location
    # First, move the gripper to the mug.
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    # Once the gripper is above the mug, grab it.
    if check("the robot's gripper is above the mug and the robot's gripper is open"):
        robot.grab("mug")
    # If the mug is still near the gripper and the gripper is closed, then we
    # have the mug.
    # Move the mug to the goal location.
    if check("the robot's gripper is near the mug and the robot's gripper is closed"):
        robot.move("mug to goal")