# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    if check("the robot's gripper does not hold the stick and the stick is not vertically aligned with the thermos"):
        robot.put("the gripper above the stick")
    if check("the stick is vertically aligned with the thermos and the robot's gripper is not near the thermos"):
        robot.push("the stick to the thermos")
    if check("the stick is near the thermos and the thermos is not aligned with the goal"):
        robot.pull("the stick and the thermos towards the goal")
    if check("the thermos is aligned with the goal"):
        robot.release("the stick and the thermos at the goal")