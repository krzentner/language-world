# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    if check("the robot's gripper is not near the stick"):
        robot.grab("stick")
    if check("the stick is not vertical"):
        robot.rotate("stick to be vertical")
    if check("the stick is not centered on the thermos lid"):
        robot.move("the stick to be above the thermos lid")
    if check("the stick is not pressing down on the thermos lid"):
        robot.push("the stick down onto the thermos lid")
    if check("the thermos is not near the target location"):
        robot.pull("the thermos to the goal location")