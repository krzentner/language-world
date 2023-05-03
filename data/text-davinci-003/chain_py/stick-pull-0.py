
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the thermos in the desired direction using the stick
    # First, put the robot's gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    # As long as the gripper is still left of the stick, grab the stick.
    if check("the robot's gripper is left of stick and the robot's gripper is open"):
        robot.put("gripper around stick")
    # Once the gripper is right of (in front of) the stick and closed, try to
    # move the thermos in the desired direction with the stick.
    # If the stick starts to slide out of the gripper, go back to the grab step.
    if check("the robot's gripper is in front of the stick and the robot's gripper is closed"):
        robot.pull("thermos with stick")