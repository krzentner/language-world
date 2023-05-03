# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Position the gripper close to the hammer
    #  2. Grab the handle of the hammer
    #  3. Position the gripper close to the nail
    #  4. Hit the nail with the hammer
    # First, position the gripper near the handle of the hammer.
    if check("the robot's gripper is not near the handle of the hammer"):
        robot.move("gripper near handle of the hammer")
    # Once the gripper is in position, grab the handle of the hammer.
    if check("the robot's gripper is near the handle of the hammer and the robot's gripper is open"):
        robot.grab("handle of the hammer")
    # Position the gripper near the nail.
    if check("the robot's gripper is not near the nail"):
        robot.move("gripper near the nail")
    # Hit the nail with the hammer.
    if check("the robot's gripper is near the nail and the hammer is grabbed"):
        robot.push("hit the nail with the hammer")