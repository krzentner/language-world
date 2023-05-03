def door_unlock(robot):
    if check("the robot's gripper is not next to the door lock"):
        robot.move("gripper to the lock")
    if check("the robot's gripper is next to the lock and not gripping the dial"):
        robot.grab("the dial on the lock")
    if check("the robot's gripper is gripping the dial on the lock"):
        robot.turn("the dial clockwise until door unlocks")