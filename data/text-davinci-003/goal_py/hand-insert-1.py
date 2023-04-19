
    # Steps:
    #  1. Put gripper into the hand
    #  2. Clamp gripper onto the hand
    # We can assume the hand is facing up, since this is a "hand-insert" task.
    # To make sure we don't bump the hand, drop the gripper into it from above.
    if check("the robot's gripper is not above the hand"):
        robot.move_gripper("above the hand")
    # Once the gripper is roughly above the hand, position it so that it is
    # around the hand (without hitting it).
    if check("the robot's gripper is not around the hand and the robot's gripper is open"):
        robot.move_gripper("around the hand", close_gripper=True)
    # If the gripper is around the hand, close the gripper so that it clamps onto
    # the hand.
    if check("the robot's gripper is around the hand"):
        robot.move_gripper("towards the target location")