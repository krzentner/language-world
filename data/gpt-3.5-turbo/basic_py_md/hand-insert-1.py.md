# hand-insert: pick up the object and move it to the target location
# def hand_insert(robot):
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is near object and the robot's gripper is open"):
        robot.close("gripper around object")
    if check("the robot's gripper is above object and the object is not aligned with the target location"):
        robot.move("the object to the target location")