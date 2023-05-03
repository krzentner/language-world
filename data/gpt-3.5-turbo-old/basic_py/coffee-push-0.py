if check("the robot's gripper is not above the coffee mug"):
        robot.place("the gripper above the coffee mug")
    if check("the robot's gripper is not around the coffee mug and the robot's gripper is open"):
        robot.drop("the gripper around the coffee mug")
    if check("the robot's gripper is near the coffee mug and the robot's gripper is open"):
        robot.close("the gripper around the coffee mug")
    if check("the robot's gripper is above the coffee mug and the robot's gripper is closed"):
        robot.place("the coffee mug at the goal location")