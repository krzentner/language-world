if check("the robot's gripper is not holding the stick"):
    robot.pickup("the stick")
if check("the robot's gripper is not near the thermos and the stick is not extending towards the thermos"):
    robot.move("the stick towards the thermos")
if check("the stick is extending towards the thermos and the robot's gripper is not near the thermos"):
    robot.grab("the thermos with the stick")
if check("the thermos is grabbed by the stick and the robot's gripper is not near the target location"):
    robot.move("the stick towards the target location")
if check("the thermos is near the target location"):
    robot.release("the thermos from the stick and place it at the target location")