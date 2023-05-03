
    if check("the robot's gripper is not near the stick and the stick is not above the robot's gripper"):
        robot.put("gripper above stick") 
    if check("the stick is above the robot's gripper and the robot's gripper is not open"):
        robot.open("gripper to grab the stick")
    if check("the robot's gripper is open and the robot's gripper is not around the stick"):
        robot.put("gripper around stick")
    if check("the robot's gripper is around the stick"):
        robot.push("stick on thermos")
    if check("the thermos is not near the goal"):
        robot.slide("thermos towards goal")