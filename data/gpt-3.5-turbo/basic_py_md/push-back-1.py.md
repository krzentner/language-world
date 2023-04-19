# push-back: slide the puck backwards to the target location
# def push_back(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
        robot.pull("the puck backwards")
    if check("the robot's gripper is near the target location while holding the puck"):
        robot.push("the puck to the goal")