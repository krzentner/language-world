
    # Steps:
    #  1. Put gripper above door lock
    #  2. Move gripper to lock wheel
    #  3. Turn wheel until the door is locked
    # First, move the gripper above the door lock.
    if check("the robot's gripper is not vertically aligned with the door lock"):
        robot.put("gripper above door lock")
    # Move the gripper to the wheel of the lock.
    if check("the robot's gripper is not near the wheel and the robot's gripper is vertically aligned with the lock wheel"):
        robot.move("gripper to wheel")
    # Until the door is locked, turn the wheel to the right.
    if check("the door is not locked"):
        robot.turn("wheel right")