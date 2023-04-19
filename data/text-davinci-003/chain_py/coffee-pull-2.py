
    # Steps:
    #  1. Put the gripper above the mug
    #  2. Grab the mug
    #  3. Pull the mug towards the target location
    # First, put the gripper above the mug to make sure we don't bump it as we
    # grab it.
    if check("the robot's gripper is not above the mug"):
        robot.put("gripper above mug")
    # If it's not around the mug, and the gripper is open, grab it.
    if check("the robot's gripper is not around mug and the robot's gripper is open"):
        robot.grab("mug")
    # Once the mug is in the gripper, start to pull it to the target location.
    if check("the robot's gripper is around mug"):
        robot.pull("mug towards target")