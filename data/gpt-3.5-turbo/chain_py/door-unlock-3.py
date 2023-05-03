# Steps:
    #  1. Put gripper around door dial handle
    #  2. Turn dial to unlock the door
    # First, put the gripper around the door dial handle.
    if check("the robot's gripper is not around the door dial handle"):
        robot.put("gripper around door dial handle")
    # Then turn the dial to unlock the door.
    if check("the robot's gripper is around the door dial handle"):
        robot.turn("dial to unlock door")