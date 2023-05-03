
    # Steps:
    #  1. Put gripper above the mug
    #  2. Grab the mug with the gripper
    #  3. Push it to the goal
    # We need to put the gripper above the mug before we can grab it because of
    # the angle of the robot's gripper.
    if check("the robot's gripper is not left of the mug"):
        robot.move_gripper("left of the mug")
    # Once the gripper is lined up left of the mug, we should be able to
    # grab the mug by moving the gripper down around it.
    if check("the robot's gripper is left of the mug and the robot's gripper is not around mug"):
        robot.move_gripper("around the mug", close_gripper=True)
    # Once the gripper is around the mug, we can just push it along to the
    # goal.
    if check("the robot's gripper is around mug"):
        robot.move_gripper("left of the target location")