if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is above the thermos and the robot's gripper is not vertically aligned with the thermos"):
        robot.put("gripper above the thermos")
    if check("the robot's gripper is vertically aligned with the thermos and the robot's gripper is not near the thermos and the robot's gripper is not holding the thermos with the stick"):
        robot.grasp("thermos with the stick")
    if check("the robot's gripper is holding the thermos with the stick"):
        robot.push("stick towards the goal with thermos")