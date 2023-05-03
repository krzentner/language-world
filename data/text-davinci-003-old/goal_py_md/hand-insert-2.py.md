

Steps:
  1. Put gripper above the puck
  2. Move gripper above the target location
  3. Drop the puck into the target location
  
If the robot's gripper is not roughly above the puck, move it to be right above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
        
If the target location is not above the puck, move the gripper to the target location.
    if check("the target location is not above the puck"):
        robot.move_gripper("above the target location")
        
If the gripper is above the target, drop the puck into the target location by slowly releasing the gripper.        
    if check("the robot's gripper is above the target location"):
        robot.move_gripper("above the puck", close_gripper=False)