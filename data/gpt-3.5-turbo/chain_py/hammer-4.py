# Steps:
    #  1. Grab the hammer with the gripper
    #  2. Move the gripper above the nail
    #  3. Swing the hammer to hit the nail
    # First, grab the hammer with the gripper.
    if check("the robot's gripper is not around the hammer"):
        robot.grab("hammer")
    # Move the gripper above the nail.
    if check("the robot's gripper is not vertically aligned with the nail and the gripper is holding the hammer"):
        robot.move("gripper above nail")
    # Swing the hammer to hit the nail.
    if check("the robot's gripper is vertically aligned with the nail and the gripper is holding the hammer"):
        robot.swing("hammer to hit nail")