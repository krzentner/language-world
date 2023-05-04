
    # Steps:
    #  1. Put gripper above the dial
    #  2. Move the gripper down so the dial is in between the fingers
    #  3. Turn the dial
    # We should make sure the gripper is above the dial first, since the dial is
    # thin.
    if check("the robot's gripper is not vertically aligned with the dial"):
        robot.move_gripper("vertically aligned with the dial", close_gripper=True)
    # If the dial is vertically aligned, move the gripper to the middle of the
    # dial.
    if check("the dial is not forward aligned with the robot's gripper"):
        robot.move_gripper("above the dial")
    # If the gripper is almost around the dial, turn the dial.
    if check("the robot's gripper is almost around the dial"):
        robot.move_gripper("horizontally aligned with the dial")

# key-insert: insert the key into the keyhole
def key_insert(robot):
    # Steps:
    #  1. Put the gripper above the key
    #  2. Move gripper around key
    #  3. Move the gripper around the keyhole
    # We should first make sure the gripper is roughly around the key.
    if check("the robot's gripper is not vertically aligned with the key"):
        robot.move_gripper("vertically aligned with the key")
    # If the gripper is above the key and not around it, put the gripper around
    # it to grab it.
    if check("the robot's gripper is vertically aligned with the key and the key is not forward aligned with the robot's gripper"):
        robot.move_gripper("near the key", close_gripper=True)
    # If the gripper is around the key, we can try to put the key in the
    # keyhole.
    if check("the key is in the robot's gripper and the robot's gripper is vertically aligned with the key"):
        robot.move_gripper("near the keyhole")

# light-switch-flip: flip the light switch
def light_switch_flip(robot):
    # Steps:
    #  1. Put gripper above the light switch
    #  2