if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
        robot.pull("the puck towards the goal while keeping the gripper around it")
    if check("the robot's gripper is in front of the goal and the puck is closer to the goal"):
        robot.push("the puck towards the goal to place it at the target location")