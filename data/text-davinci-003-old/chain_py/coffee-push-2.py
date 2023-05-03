
    # Steps:
    #  1. Put gripper above mug
    #  2. Drop gripper so it's around mug
    #  3. Close gripper to grab mug
    #  4. Move mug to target
    # First, move the gripper into position above the mug.
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    # The next step is to close the gripper. Make sure the mug is aligned with
    # the gripper.
    if check("the robot's gripper is not vertically aligned with mug and the robot's gripper is open"):
        robot.drop("gripper around mug")
    # If the mug is aligned with the gripper, we can close the gripper around it
    # so that it's held.
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # If the gripper is closed and the mug is still near the gripper, the robot
    # probably has it. Move the mug (with the gripper carrying it) to the target
    # location.
    if check("the robot's gripper is closed around mug and the mug is below the robot's gripper"):
        robot.move("mug to target")