
    if check("the robot's gripper is not above the mug and the robot's gripper is not vertically aligned with the mug"):
       robot.put("the gripper above the mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not around the mug"):
        robot.grab("the mug")
    if check("the robot's gripper is around the mug and the goal is not before the robot's gripper"):
        robot.pull("the mug to the goal")