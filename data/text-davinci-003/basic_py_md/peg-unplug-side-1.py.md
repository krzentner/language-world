

If check("the robot's gripper is not vertically aligned with the peg"):
    robot.put("gripper above peg")
    
If check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
    robot.grab("peg")
  
If check("the robot's gripper is forward aligned with the peg and peg is horizontally aligned with hole"):
    robot.pull("peg away from hole")