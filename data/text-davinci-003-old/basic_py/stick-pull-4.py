
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the robot's gripper is near the stick and the robot's gripper is not above the thermos"):
        robot.move("gripper above the thermos")
    if check("the robot's gripper is above the thermos and the thermos is not near the target location"):
        robot.push("the stick to the thermos")
    if check("thermos is near target location and the robot's gripper is not gripping stick"):
        robot.pull("the stick to move the thermos to target location")