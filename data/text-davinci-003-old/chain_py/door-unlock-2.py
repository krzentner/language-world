
    # Steps:
    #  1. Put gripper above door handle
    #  2. Line up gripper to the door lock
    #  3. Turn the dial
    # To start unlocking the door, we first need to line up the gripper with the
    # locking mechanism on the door.
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the gripper is roughly lined up with the door lock, we can rotate the
    # dial to unlock it.
    if check("the robot's gripper is near the door handle and the robot's gripper is not horizontally aligned with the door lock"):
        robot.align("gripper to the lock")
    # If the gripper is aligned with the door lock, rotate the dial back and
    # forth a few times to unlock it.
    if check("the robot's gripper is horizontally aligned with the door lock"):
        robot.rotate("dial a few times to unlock")