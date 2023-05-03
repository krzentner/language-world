
    # Steps:
    #  1. Put gripper slightly above the nail
    #  2. Move the gripper down to the nail and close the gripper
    #  3. Hit the nail
    # Put the gripper slightly above the nail, so we can move down around it
    # and close the gripper.
    if check("the robot's gripper is not slightly above the nail"):
        robot.move_gripper("slightly above the nail")
    # Once the gripper is above the nail, move the gripper near it and close the
    # gripper. This will grab the nail and keep it between the gripper and the
    # hammer.
    if check("the robot's gripper is slightly above the nail and the robot's gripper is not closed"):
        robot.move_gripper("near the nail", close_gripper=True)
    # Finally, hit the nail. The robot doesn't need to be precise with where
    # it's hitting, so just move the gripper up and down.
    if check("the robot's gripper is near the nail and the robot's gripper is closed"):
        robot.move_gripper("above the nail")
        robot.move_gripper("below the nail")