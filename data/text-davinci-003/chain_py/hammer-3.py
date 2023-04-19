
    # Steps:
    #  1. Put gripper above hammer and nail
    #  2. Put gripper forwardly aligned with handle of hammer
    #  3. Push hammer straight down onto nail
    # First, put the gripper above the nail and the hammer.
    if check("the robot's gripper is not above the hammer and the nail"):
        robot.place("gripper above hammer and nail")
    # If the gripper is lined up from above, and the gripper is not forwardly
    # aligned, align the gripper with the handle of the hammer.
    if check("the robot's gripper is above the hammer and the nail and the robot's gripper is not forwardly aligned with the handle of the hammer"):
        robot.align("gripper with the handle of the hammer")
    # If the gripper is lined up with the handle of the hammer, we can just push
    # it straight down onto the nail.
    if check("the robot's gripper is forwardly aligned with the handle of the hammer"):
        robot.push("hammer straight down onto nail")