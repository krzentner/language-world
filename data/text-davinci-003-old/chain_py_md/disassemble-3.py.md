

Steps:
  1. Put the gripper below the wrench
  2. Push the wrench downwards from the bottom
  3. Pull the wrench off the peg

if check("the robot's gripper is not below the wrench and the wrench is above the peg"):
    robot.put("gripper below wrench")
if check("the robot's gripper is below the wrench and the wrench is above the peg"):
    robot.push("down on wrench")
if check("the wrench is near the robot's gripper and the robot's gripper is at the bottom of the wrench"):
    robot.pull("wrench off of peg")