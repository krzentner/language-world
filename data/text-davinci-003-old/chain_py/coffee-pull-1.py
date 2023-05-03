
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Pull the mug closer
    # We need to put the gripper above the mug handle before we can grab it, 
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.put("gripper above mug handle")
    # Once the gripper is lined up above the mug handle, we should be able to
    # grab the mug handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with mug handle and the robot's gripper is not around mug handle"):
        robot.drop("gripper around mug handle")
    # Now that the gripper is around the mug handle, we can just pull the mug 
    # closer.
    # If the mug isn't close enough, move the mug closer by repeating this step.
    if check("the robot's gripper is around mug handle"):
        robot.pull("mug closer")