# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper on dial
    #  2. Turn dial to the unlocked position
    # The robot needs to turn the dial to the right position to unlock the door.
    # If the gripper is not above the dial, move it there.
    if check("the robot's gripper is not above the door dial"):
        robot.move_gripper("above the door dial")
    # If the gripper is above the dial but not around it, move it around the dial.
    if check("the robot's gripper is above the door dial and the robot's gripper is open"):
        robot.move_gripper("around the door dial", close_gripper=True)
    # Move the dial to the unlocked position (one full turn to the right).
    if check("the robot's gripper is around the door dial and not in the unlocked position"):
        robot.move_gripper("one full turn to the right")