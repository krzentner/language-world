

if check("the robot's gripper is not near the button and the wall is blocking the robot's gripper"):
    robot.move("gripper to the left of the wall")
if check("the robot's gripper is near the button and the wall is blocking the robot's gripper"):
    robot.put("gripper at one end of the wall")
if check("the robot's gripper is close to the button and the wall is not blocking the robot's gripper"):
    robot.push("gripper onto the button")