# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Move gripper to dial
    #  2. Grab dial with gripper
    #  3. Turn dial to the right until unlocked
    # Move the gripper to the dial on the door.
    if check("the robot's gripper is not near the dial"):
        robot.move("gripper to dial")
    # Grab the dial with the gripper.
    if check("the robot's gripper is near the dial and the robot's gripper is open"):
        robot.grab("dial")
    # Turning the dial to the right until unlocked.
    if check("the dial is locked"):
        robot.turn("dial to the right until unlocked")