

If check("the robot's gripper is not near the door handle"):
    robot.put("gripper above door handle")
If check("the robot's gripper is near the door handle"):
    robot.grab("door handle")
If check("the robot's gripper is forward aligned with door handle"):
    robot.push("door towards goal")