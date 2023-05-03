if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and there is a wall blocking the way"):
        robot.lift("the gripper")
        robot.move("the gripper to left of wall")
        robot.place("the gripper above puck")
        robot.drop("gripper around puck")
        robot.close("gripper around puck")
        robot.lift("the gripper")
        robot.move("the gripper to right of wall")
        robot.place("the puck at goal")