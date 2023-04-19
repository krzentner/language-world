# Steps:
   # 1. Move gripper above the plate
   # 2. Close gripper around the plate
   # 3. Slide the plate towards the target location.
   # Put the gripper roughly above the plate.
   if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
   # If the gripper is not around the plate, put it around the plate.
   if check("the robot's gripper is not around the plate and the robot's gripper is open"):
       robot.move_gripper("near the plate", close_gripper=True)
   # If the gripper is near the plate and closed, slide the plate towards the target location.
   if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
       robot.move_gripper("above the target location")