# door-unlock: turn the dial on the door
# def door_unlock(robot):
    if check("the robot's gripper is not above the dial"):
        robot.place("gripper above dial")
    if check("the robot's gripper is above the dial and the robot's gripper is not around the dial"):
        robot.drop("gripper around the dial")
    if check("the robot's gripper is around the dial and the robot's gripper is not gripping the dial tightly"):
        robot.close("gripper around the dial tightly")
    if check("the robot's gripper is gripping the dial tightly and the dial is not unlocked"):
        robot.rotate("dial to the correct combination")
        robot.open("door")