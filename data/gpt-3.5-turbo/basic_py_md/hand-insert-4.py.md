# hand-insert: pick up the object and insert it into the hole using hand dexterity
def hand_insert(robot):
    if check("the robot's gripper is not vertically aligned with the object"):
        robot.put("gripper above object")
    if check("object is not above the robot's gripper and the gripper is open"):
        robot.drop("gripper open")
    if check("the robot's gripper is above the object and the gripper is closed"):
        robot.pick("object using hand dexterity")
    if check("the robot's gripper is above the hole and the object is not vertically aligned with the hole"):
        robot.align("object to the hole using hand dexterity")
    if check("the object is vertically aligned with the hole"):
        robot.insert("object into the hole using hand dexterity")