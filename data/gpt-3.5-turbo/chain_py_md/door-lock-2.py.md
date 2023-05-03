# door-lock: turn the dial on the door
def door_lock(robot):
    # Steps:
    #  1. Position gripper near the dial
    #  2. Close gripper around the dial
    #  3. Turn the dial to the correct numbers
    #  4. Release the dial and open the gripper
    # Position the gripper near the dial
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper near dial")
    # Close the gripper around the dial
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.close("gripper around dial")
    # Turn the dial to the correct numbers
    if check("the dial is not at the correct numbers"):
        robot.turn("dial to correct numbers")
    # Release the dial and open the gripper
    if check("the gripper is around the dial and the dial is at the correct numbers"):
        robot.release("dial")
        robot.open("gripper")