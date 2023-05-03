
    # Steps:
    #  1. Put the robot's gripper above the hammer
    #  2. Drop robot's gripper around the hammer
    #  3. Raise the hammer above the nail
    #  4. Strike the nail with the hammer
    # First, put the robot's gripper roughly above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above hammer")
    # Once the gripper is properly lined up, grab the hammer.
    if check("the robot's gripper is vertically aligned with the hammer and the robot's gripper is not around the hammer"):
        robot.drop("gripper around hammer")
    # Now that the robot has the hammer, raise it above the nail.
    if check("the robot's gripper is around the hammer and the hammer is not above the nail"):
        robot.raise("hammer above nail")
    # Finally, hit the nail with the hammer.
    if check("the hammer is above the nail"):
        robot.strike("nail with hammer")