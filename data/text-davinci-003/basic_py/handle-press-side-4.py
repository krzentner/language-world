
     if check("the robot's gripper is not at side of handle"):
        robot.move("gripper to side of handle")
     if check("the robot's gripper is at side of handle"):
        robot.push("down on handle")