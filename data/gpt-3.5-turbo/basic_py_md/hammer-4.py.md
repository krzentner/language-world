# hammer: hit the nail with the hammer
# def hammer(robot):
if check("the hammer is not in the robot's gripper"):
    robot.grab("the hammer")
if check("the hammer is in the robot's gripper and the robot's gripper is not above the nail"):
    robot.reach("the nail")
if check("the nail is in front of the robot's gripper and the hammer is above the nail"):
    robot.push("the hammer down onto the nail")