# Steps:
    #  1. Put gripper around doorknob
    #  2. Turn doorknob to open door
    # To open a door, we need to turn the doorknob. This requires the gripper to be
    # around the doorknob.
    # If the gripper is not initially around the doorknob, move it to be around
    # the doorknob.
    if check("the robot's gripper is not around doorknob"):
        robot.move_gripper("around the doorknob", close_gripper=True)
    # If the gripper is around the doorknob, turn the doorknob to open the door.
    if check("the robot's gripper is around doorknob"):
        robot.turn_gripper("open the door")