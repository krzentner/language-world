
    # Steps:
    #  1. Put gripper near front of the puck
    #  2. Push gripper into the puck
    #  3. Slide the puck to goal
    # Since the robot is pushing the pupck backwards, we need to put the gripper
    # as close to the front of the puck as possible.
    if check("the robot's gripper is not at the front of puck"):
        robot.move_gripper("at the front of puck")
    # Once the gripper is close to the puck, just push the puck to the target
    # location.
    if check("the robot's gripper is at the front of puck"):
        robot.move_gripper("above the target location")