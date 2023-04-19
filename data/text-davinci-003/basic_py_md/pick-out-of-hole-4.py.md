

If check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
If check("the peg is not left of the robot's gripper and the peg is not forward aligned with the robot's gripper"):
    robot.grab("peg")
If check("the robot's gripper is forward aligned with the peg"):
    robot.pick("peg out of the hole")
If check("the peg is below the robot's gripper and the peg is not near the goal"):
    robot.place("gripper above the peg")
If check("the robot's gripper is near the goal and the robot's gripper is open"):
    robot.close("gripper around the peg")
If check("the robot's gripper is above the peg and the robot's gripper is closed"):
    robot.place("peg at the goal")