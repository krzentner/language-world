# Steps:
    #  1. Pick up the hammer
    #  2. Position the hammer above the nail
    #  3. Swing the hammer down onto the nail
    #  4. Pick up the hammer again
    # First, pick up the hammer if it's not already in the robot's gripper.
    if check("the hammer is not in the robot's gripper"):
        robot.grab("the hammer")
    # Position the gripper above the nail.
    if check("the robot's gripper is not above the nail"):
        robot.put("gripper above the nail")
    # Swing the hammer down onto the nail.
    if check("the robot's gripper is above the nail"):
        robot.swing("the hammer onto the nail")
    # Pick up the hammer again.
    if check("the hammer is not in the robot's gripper"):
        robot.grab("the hammer")