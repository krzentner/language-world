if check("the robot's gripper is not near the handle"):
        robot.move("gripper near handle")
    if check("the robot's gripper is next to the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    if check("the robot's gripper is around the handle and the handle is not in the down position"):
        robot.push("down on handle")