# door-unlock: turn the dial on the door
def door_unlock(robot):
    # Steps:
    #  1. Move the gripper to the dial
    #  2. Grab the dial with the gripper
    #  3. Turn the dial clockwise until it stops
    # First, move the gripper to the dial.
    if check("the robot's gripper is not near the door dial"):
        robot.move("gripper to door dial")
    # Once the gripper is near the dial, grab it.
    if check("the robot's gripper is near door dial and the robot's gripper is not around door dial"):
        robot.grab("door dial")
    # Once the gripper is around the dial, turn it.
    if check("the robot's gripper is around door dial"):
        robot.turn("dial clockwise until it stops")