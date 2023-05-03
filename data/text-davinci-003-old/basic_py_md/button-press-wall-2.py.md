

If check("the robot's gripper is not vertically aligned with the button and the robot's gripper is far from the short wall"):
    robot.put("gripper above button and close to the short wall")
if check("the robot's gripper is forward aligned with the button and the robot's gripper is close to the short wall"):
    robot.push("gripper into the short wall")
if check("the robot's gripper is above button and the robot's gripper is pushed up against the short wall"):
    robot.push("down on button")