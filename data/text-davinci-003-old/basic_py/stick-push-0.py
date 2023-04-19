
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is around the stick and the stick is not horizontally aligned with the thermos"):
        robot.align("stick to thermos")
    if check("the stick is horizontally aligned with the thermos"):
        robot.push("stick towards goal")