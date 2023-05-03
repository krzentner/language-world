# Steps:
    #  1. Pick up the hammer
    #  2. Position the hammer above the nail
    #  3. Swing the hammer down to hit the nail
    # First, pick up the hammer if the gripper is not already holding it.
    if check("the robot's gripper is not holding the hammer"):
        robot.pickup("hammer")
    # Next, position the hammer above the nail.
    # We can assume the nail is already in place.
    if check("the robot's gripper is not directly above the nail"):
        robot.align("hammer above nail")
    # Once the hammer is aligned with the nail, swing it down to hit the nail.
    if check("the robot's gripper is directly above the nail"):
        robot.swing("hammer down")