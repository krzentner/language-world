# Steps:
    #  1. Put the gripper near the end of the stick
    #  2. Grab the handle of the thermos with the gripper
    #  3. Slide the thermos towards the target using the stick
    # First, put the gripper near the end of the stick.
    if check("the robot's gripper is not near the end of the stick"):
        robot.move("gripper near the end of the stick")
    # If the gripper is near the end of the stick but not around the thermos
    # handle, move the gripper around the handle.
    if check("the robot's gripper is near the end of the stick but is not around the thermos handle"):
        robot.grab("thermos handle with gripper")
    # Once we have the thermos handle, use the stick to slide it towards the
    # target location.
    if check("the robot's gripper is around the thermos handle with the stick and the thermos is not at the target location"):
        robot.slide("the thermos towards the target using the stick")