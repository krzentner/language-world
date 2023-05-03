# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
    #  1. Position the gripper above the nail
    #  2. Drop the hammer onto the nail
    #  3. Lift the hammer off the nail
    # First, align the gripper above the nail.
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.move_gripper("vertically aligned with the nail")
    # Once the gripper is lined up above the nail, drop the hammer onto the nail
    # by closing the gripper.
    if check("the robot's gripper is vertically aligned with the nail and the robot's gripper is open"):
        robot.move_gripper("above the nail", close_gripper=True)
    # After the hammer is dropped onto the nail, lift it up by opening the
    # gripper again.
    if check("the robot's gripper is above the nail and the robot's gripper is closed"):
        robot.move_gripper("vertically aligned with the nail", close_gripper=False)