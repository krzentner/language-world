# box-close: pick up the box lid and place it on the box
# def box_close(robot):
   # Steps:
   # 1. Put gripper above the lid
   # 2. Grab the lid with the gripper
   # 3. Move the gripper above the box
   # 4. Place the lid on the box
   # First, put the gripper above the lid.
   if check("the robot's gripper is not vertically aligned with the lid"):
        robot.move_gripper("vertically aligned with the lid")
   # If the gripper isn't around the lid, put it around the lid.
   if check("the robot's gripper is not around the lid and the robot's gripper is open"):
        robot.move_gripper("near the lid", close_gripper=True)
   # If the gripper is around the lid and closed, move the gripper above the box.
   if check("the robot's gripper is around the lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
   # If the gripper is above the box, release the lid into the box.
   if check("the robot's gripper is above the box"):
        robot.move_gripper("around the lid", close_gripper=False) 
        robot.move_gripper("near the target location")