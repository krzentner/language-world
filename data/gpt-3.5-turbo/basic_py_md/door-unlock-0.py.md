# door-unlock: turn the dial on the door
# def door_unlock(robot):
    if check("the robot's gripper is not close to the door handle"):
        robot.reach("to the door handle")
    if check("the robot's gripper is not almost vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is not closed"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is closed around the door handle and the dial is not set to the correct combination"):
        robot.turn("dial to the correct combination")
    if check("the dial is set to the correct combination"):
        robot.pull("the door open")