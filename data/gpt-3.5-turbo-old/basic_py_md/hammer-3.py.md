# hammer: hit the nail with the hammer
# def hammer(robot):
if check("the robot's gripper is not above the hammer and the hammer is not close to the nail"):
    robot.move("gripper above the hammer")
    robot.grab("the hammer")
    robot.move("gripper above the nail")
if check("the hammer is above the nail and the robot's gripper is holding the hammer"):
    robot.push("hammer to hit the nail")
    robot.move("gripper away from the nail and the hammer")
    robot.drop("the hammer")