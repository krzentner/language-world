
    if check("the robot's gripper is not vertical aligned with coffee mug and the robot's gripper is not forward aligned with coffee mug"):
        robot.put("gripper above coffee mug")
    if check("the robot's gripper is forward aligned with coffee mug"):
        robot.grab("coffee mug")
    if check("the robot's gripper is around coffee mug and the mug is not left of the robot"):
        robot.shift("mug to the left")
    if check("the robot's gripper is around coffee mug and mug is left of the robot"):
        robot.push("coffee to the goal")