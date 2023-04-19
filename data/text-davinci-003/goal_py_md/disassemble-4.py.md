

Steps:
  1. Move gripper to above the wrench
  2. Move gripper near the wrench and pinch it with the gripper
  3. Pivot the wrench and pull it off the peg
  
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench", close_gripper=True)
    # Once the gripper is lined up with the wrench, pinch the handle of the wrench 
    # with the gripper.
    if check("the robot's gripper is vertically aligned with the wrench"):
        robot.move_gripper("above thepeg")
    # Once the wrench is firmly in the grip of the robot's gripper, begin to pivot
    # the wrench and pull it off the peg. 
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("vertically aligned with the wrench")