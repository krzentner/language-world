# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the hammer near the nail
    #  2. Grab the hammer
    #  3. Raise the hammer
    #  4. Swing the hammer down to hit the nail
    #  5. Release the hammer
    # First, move the gripper to put the hammer near the nail.
    if check("the robot's gripper is not near the nail"):
        robot.reach("the hammer to the nail")
    # Once the gripper is near the hammer, grab it.
    if check("the robot's gripper is near the hammer and the robot's gripper is open"):
        robot.close("gripper around hammer")
    # Once we have the hammer, lift it up to prepare for a swing.
    if check("the robot's gripper is holding the hammer and the hammer is not raised"):
        robot.lift("the hammer")
    # Now that the hammer is lifted, we can strike the nail with a swing.
    if check("the robot's gripper is holding the hammer and the hammer is raised"):
        robot.swing("the hammer down onto the nail")
    # Once the hammer has hit the nail, release it so we can move on to the
    # next task.
    if check("the robot's gripper is holding the hammer and the hammer is touching the nail"):
        robot.release("the hammer")