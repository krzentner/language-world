# hand-insert: pick up the object and move it to the target location
def hand_insert(robot):
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is near object and the robot's gripper is open"):
        robot.close("gripper around object")
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        if check("the robot's gripper is not vertically aligned with the hole"):
            robot.put("gripper above the hole")
        if check("the robot's gripper is vertically aligned with the hole and the object is not horizontally aligned with the hole"):
            robot.align("object to the hole")
        if check("object is horizontally aligned with hole"):
            robot.insert("object into hole")