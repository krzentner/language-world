if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around the stick"):
        robot.grab("stick")
    if check("the robot's gripper is around the stick and the stick is not near the thermos"):
        robot.pull("stick towards thermos")
    if check("the robot's gripper is around the stick and the stick is near the thermos and the robot's gripper is not vertically aligned with the thermos"):
        robot.put("gripper above thermos")
    if check("the robot's gripper is vertically aligned with the thermos and the robot's gripper is not around the thermos"):
        robot.grab("thermos")
    if check("the robot's gripper is around the thermos and the thermos is not at the goal"):
        robot.pull("thermos towards goal")
    if check("the thermos is at the goal"):
        robot.release("thermos and stick")