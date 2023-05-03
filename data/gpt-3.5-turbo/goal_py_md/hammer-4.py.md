# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Move the gripper above the hammer
    #  2. Close the gripper to pick up the hammer
    #  3. Move the gripper to position the hammer over the nail
    #  4. Move the hammer down to hit the nail
    #  5. Lift the hammer back up
    #  6. Open the gripper to release the hammer
    # First, place the gripper above the hammer to grab it.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.move_gripper("vertically aligned with the hammer")
    # If the gripper is aligned with the hammer but not near it, move the gripper
    # down to the hammer to pick it up.
    if check("the robot's gripper is vertically aligned with the hammer and the robot's gripper is not near the hammer"):
        robot.move_gripper("near the hammer", close_gripper=True)
    # If the gripper is holding the hammer, position it over the nail.
    if check("the robot's gripper is holding the hammer and the robot's gripper is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail")
    # Move the hammer down to hit the nail.
    if check("the robot's gripper is holding the hammer and the robot's gripper is vertically aligned with the nail and the robot's gripper is not above the nail"):
        robot.move_gripper("above the nail")
    if check("the robot's gripper is holding the hammer and the robot's gripper is above the nail"):
        robot.move_gripper("touching the nail")
    # Lift the hammer back up.
    if check("the robot's gripper is touching the nail"):
        robot.move_gripper("above the nail")
    # Open the gripper to release the hammer.
    if check("the robot's gripper is above the nail and the robot's gripper is holding the hammer"):
        robot.move_gripper("near the hammer", close_gripper=False)