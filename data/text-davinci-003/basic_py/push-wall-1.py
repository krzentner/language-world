
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper and the puck is next to the wall"):
        robot.shift("the puck away from wall")
    if check("the puck is away from the wall and the puck is not near the target location"):
        robot.slide("the puck to the goal")