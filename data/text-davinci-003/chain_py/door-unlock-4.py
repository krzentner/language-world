
    # Steps:
    #  1. Put gripper above the lock dial
    #  2. Turn the dial
    #  3. Turn the dial harder
    # First, put the gripper above the lock dial.
    if check("the robot's gripper is not vertically aligned with lock dial"):
        robot.put("gripper above lock dial")
    # If the gripper is vertically aligned with the lock dial and not close to
    # it, move the gripper down to the lock dial.
    if check("the robot's gripper is vertically aligned with lock dial and the robot's gripper is not near the lock dial"):
        robot.move("gripper to lock dial")
    # If the gripper is near the lock dial, the robot can start turning it.
    if check("the robot's gripper is near the lock dial"):
        robot.turn("lock dial")
    # If the lock dial is starting to be hard to turn, pressing harder should help.
    if check("the lock dial is hard to turn"):
        robot.push("lock dial harder")