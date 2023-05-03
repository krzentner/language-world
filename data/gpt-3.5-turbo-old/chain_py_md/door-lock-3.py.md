# door-lock: turn the dial on the door
# def door_lock(robot):
    # Steps:
    #  1. Put gripper on dial
    #  2. Turn dial to the right number
    #  3. Close the lock
    # Place the gripper on the dial.
    if check("the robot's gripper is not on the dial"):
        robot.put("gripper on the dial")
    # Turn the dial to the correct number, assuming the number is 5.
    if check("the dial is not pointed to 5"):
        robot.turn("dial to 5")
    # Close the lock.
    if check("the lock is not closed"):
        robot.close("lock")