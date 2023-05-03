
    if check("the robot's gripper is not above coffee mug and the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above coffee mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around coffee mug"):
        robot.put("gripper around coffee mug")
    if check("the robot's gripper is around coffee mug and the mug is not near the goal"):
        robot.push("the mug to the goal")
    if check("the mug is near the goal"):
        robot.release("the mug at goal")