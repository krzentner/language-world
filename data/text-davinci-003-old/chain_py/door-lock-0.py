
    # Steps:
    #  1. Put gripper above the lock
    #  2. Grab the lock with the gripper
    #  3. Turn the dial on the lock
    # We need to make sure the robot is near the lock.
    if check("the robot's gripper is not near the lock"):
        robot.put("gripper above lock")
    # Once the robot is closer to the lock, it can grab the lock with its
    # gripper.
    if check("the robot's gripper is near the lock and the robot's gripper is not grabbing the lock"):
        robot.grab("lock")
    # Once the robot has grabbed the lock, it can start turning the dial.
    if check("the robot's gripper is grabbing the lock"):
        robot.turn("dial on lock")