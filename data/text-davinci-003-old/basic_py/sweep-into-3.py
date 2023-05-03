
    if check("the object is not above the robot's gripper"):
        robot.move("gripper above object")
    if check("the robot's gripper is above the object and the distance between gripper and object is more than one"):
        robot.sweep("object towards gripper")
    if check("the distance between gripper and object is one"):
        robot.grab("object")
    if check("the object is in the robot's gripper"):
        robot.place("object at target")