# hammer: hit the nail with the hammer
# def hammer(robot):
    # Steps:
    #  1. Put the gripper above the hammer
    #  2. Grab the hammer with the gripper
    #  3. Align the hammer with the nail
    #  4. Hit the nail with the hammer
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not vertically aligned with the hammer"):
        robot.put("gripper above hammer")
    # If the hammer isn't in the gripper, grab it.
    if check("the robot's gripper is not around the hammer and the robot's gripper is open"):
        robot.grab("hammer")
    # If the hammer is in the gripper but not aligned with the nail, align it.
    if check("the hammer is in the gripper and the hammer is not aligned with the nail"):
        robot.align("hammer with the nail")
    # If the hammer is aligned with the nail and the gripper is above the nail,
    # hit the nail with the hammer.
    if check("the hammer is aligned with the nail and the robot's gripper is above the nail"):
        robot.hit("hammer into the nail")