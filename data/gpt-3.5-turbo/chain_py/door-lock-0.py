# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Put gripper on dial
    #  2. Turn the dial a certain number of times
    # Because most door locks have a cylindrical dial, we just need to move the
    # gripper onto the dial and turn it a specific number of times.
    # Move the gripper to the dial.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    # Twist the dial a certain number of times in one direction to lock it.
    robot.twist("dial", "clockwise", 3)