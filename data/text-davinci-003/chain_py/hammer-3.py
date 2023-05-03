
    # Steps:
    #  1. Put gripper above the hammer
    #  2. Close gripper around the hammer
    #  3. Move the hammer above the nail
    #  4. Drop the hammer onto the nail
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above the hammer")
    # If the gripper is near the hammer, move it around the hammer to close it.
    if check("the robot's gripper is near the hammer and the robot's gripper is open"):
        robot.grab("hammer")
    # Once the gripper is closed and the hammer is directly below the gripper,
    # just move the gripper directly above the nail and drop the hammer there.
    if check("the robot's gripper is above hammer and the hammer is directly below the robot's gripper and the hammer is not above the nail"):
        robot.put("hammer above nail")
    # If the hammer is directly above the nail and the gripper is closed around
    # the hammer, drop the hammer onto the nail.
    if check("the hammer is directly above the nail and the robot's gripper is closed around the hammer"):
        robot.drop("hammer onto nail")