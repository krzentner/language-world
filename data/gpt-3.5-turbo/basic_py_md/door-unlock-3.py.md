# door-unlock: turn the dial on the door
# def door_unlock(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.move("gripper to the right of the door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.turn("dial clockwise")
    if check("the dial has turned fully"):
        robot.release("door handle")