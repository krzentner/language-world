# hammer: hit the nail with the hammer
# def hammer(robot):
if check("the hammer is not held in the robot's gripper"):
    robot.grab("the hammer")
if check("the robot's gripper is not above the nail"):
    robot.move("the gripper above the nail")
if check("the hammer is not aligned with the nail"):
    robot.align("the hammer with the nail")
if check("the hammer is not hitting the nail"):
    robot.push("the hammer onto the nail")