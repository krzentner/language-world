

Steps:
  1. Put gripper above the box lid
  2. Drop gripper around the box lid
  3. Close gripper around the box lid
  4. Move the box lid to the box
  5. Place the box lid onto the box

# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the box lid
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    #  2. Drop gripper around the box lid
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.move_gripper("near the box lid", close_gripper=True)
    #  3. Close gripper around the box lid
    if check("the robot's gripper is around the box lid and the robot's gripper is closed"):
        robot.move_gripper("above the box")
    #  4. Move the box lid to the box
    if check("the robot's gripper is above the box and the box lid is not above the box"):
        robot.move_gripper("above the box lid")
    #  5. Place the box lid onto the box
    if check("the robot's gripper is above the box lid"):
        robot.move_gripper("above the box")