
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.drop("gripper around stick")
    if check("the robot's gripper is around the stick and the robot's gripper is closed and the thermos is not near the robot's gripper"):
        robot.move("the robot with the stick to the thermos")
    if check("the robot's gripper is around the stick and the robot's gripper is closed and the thermos is near the robot's gripper"):
        robot.push("the thermos to the goal")