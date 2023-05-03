# Steps:
    #  1. Put gripper near the hammer and open it
    #  2. Pick up the hammer with the gripper
    #  3. Line the hammer up with the nail
    #  4. Swing the hammer down onto the nail
    # First, put the gripper near the hammer to pick it up.
    if check("the robot's gripper is not near the hammer"):
        robot.place("gripper near hammer")
    # Once the gripper is near the hammer, open it and try to grab the hammer.
    if check("the robot's gripper is near the hammer and the robot's gripper is open"):
        robot.grab("hammer")
    # If we successfully grabbed the hammer, line it up with the nail.
    if check("the robot's gripper is around the hammer"):
        robot.align("hammer to nail")
    # If the hammer is lined up with the nail, swing the hammer down onto it.
    if check("the hammer is aligned with the nail"):
        robot.swing("hammer down onto nail")