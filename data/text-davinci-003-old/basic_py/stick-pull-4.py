
    if check("the robot's gripper is not above the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is not around the stick"):
        robot.drop("gripper around stick")
    if check("the robot's gripper is around the stick and the robot's gripper is not above the thermos") :
        robot.move("stick to thermos")
    if check("the robot's gripper is above the thermos and the thermos is below the robot's gripper"):
        robot.pull("the thermos with the stick to target location")