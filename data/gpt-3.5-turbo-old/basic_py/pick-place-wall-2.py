if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        if check("the wall is between the robot's gripper and the goal"):
            robot.move("gripper to the side of the wall")
        if check("the gripper is beside the wall and the gripper is not above the goal"):
            robot.move("gripper above the goal")
        if check("the gripper is above the goal and the gripper is not touching the wall"):
            robot.move("gripper to the wall")
        if check("the gripper is against the wall and the gripper is above the goal"):
            robot.place("puck at goal")