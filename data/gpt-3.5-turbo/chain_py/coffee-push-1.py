# Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Move the mug to the target location by pushing it
    # First, put the gripper above the mug.
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above mug")
    # If the mug becomes left of the gripper, go back to putting the gripper
    # above the mug.
    if check("mug is not left of the robot's gripper and mug is not forward aligned with the robot's gripper"):
        robot.grab("mug")
    # Once the gripper is around the mug, we can push it to the target location.
    # Determine the direction to move the mug based on the position of the grip-
    # per relative to the goal.
    if check("the robot's gripper is around the mug"):
        if check("the goal is to the right of the gripper"):
            robot.push("mug to the right")
        elif check("the goal is to the left of the gripper"):
            robot.push("mug to the left")
        elif check("the goal is above the gripper"):
            robot.push("mug up")
        elif check("the goal is below the gripper"):
            robot.push("mug down")