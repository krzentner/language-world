


    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is aligned with the door handle"):
        robot.put("push door towards goal")
    if check("the door is aligned with the goal"):
        robot.push("firmly on door to close")