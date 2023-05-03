if check("the robot's gripper is not almost horizontally aligned with the stick and the robot's gripper is not near the stick"):
        robot.put("gripper near the stick")
        robot.move("gripper to the side of the stick")
    if check("the robot's gripper is almost horizontally aligned with the stick and the robot's gripper is not around the stick"):
        robot.grab("the stick")
    if check("the robot's gripper is around the stick and the robot's gripper is not aligned with the thermos"):
        robot.align("stick to the thermos")
    if check("the robot's gripper is aligned with the thermos and the robot's gripper is not almost horizontally aligned with the thermos"):
        robot.move("gripper to side of thermos")
    if check("the robot's gripper is almost horizontally aligned with the thermos and the robot's gripper is not near the thermos"):
        robot.move("gripper near the thermos")
    if check("the robot's gripper is near the thermos and the robot's gripper is not under it"):
        robot.put("gripper under the thermos")
    if check("the robot's gripper is under the thermos"):
        robot.push("thermos towards the goal")