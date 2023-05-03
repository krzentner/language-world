
    # Steps:
    #  1. Put gripper above the object
    #  2. Grab object with gripper
    #  3. Move the object to the target location
    # First, put the gripper over the object.
    if check("the robot's gripper is not above the object"):
        robot.put("the gripper above the object")
    # Now close the gripper around the object.
    if check("the robot's gripper is not closed around the object"):
        robot.grab("the object")
    # If the gripper is closed, try and move the object to the target location.
    if check("the robot's gripper is closed around the object"):
        robot.move("the object to the goal")