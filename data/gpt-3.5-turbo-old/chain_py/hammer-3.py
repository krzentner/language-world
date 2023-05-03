# Steps:
    #  1. Grip the hammer
    #  2. Move to position above the nail
    #  3. Swing hammer down to hit the nail
    # If the gripper is not holding the hammer, we should grip it first.
    if check("the robot's gripper is not holding the hammer"):
        robot.grab("hammer")
    # If the gripper is not above the nail, move it above the nail.
    if check("the robot's gripper is not above the nail"):
        robot.move("gripper above nail")
    # If the gripper is above the nail now, swing the hammer down to hit it.
    if check("the robot's gripper is above the nail"):
        robot.swing("hammer down on the nail")