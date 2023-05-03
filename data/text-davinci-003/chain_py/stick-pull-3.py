
    # Steps:
    #  1. Put the gripper above the stick
    #  2. Grab the stick
    #  3. Line up the stick with the handle of the thermos
    #  4. Pull the thermos to the goal
    # First, put the gripper above the stick, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above stick"):
        robot.grab("gripper above stick")
    # If the gripper wasn't over the stick, we should be able to grab the stick
    # now.
    # Because the stick is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the robot's gripper is not left of the stick and the robot's gripper is not forward aligned with the stick"):
        robot.grab("stick")
    # Once the stick is in the gripper, line it up with the handle of the
    # thermos.
    if check("the robot's gripper is forward aligned with the stick and the stick is not horizontally aligned with thermos handle"):
        robot.align("stick to thermos handle")
    # Once the stick is lined up with the handle of the thermos, the robot can
    # pull the thermos to the goal.
    if check("the robot's gripper is forward aligned with the stick and the stick is horizontally aligned with thermos handle"):
        robot.pull("thermos to goal")