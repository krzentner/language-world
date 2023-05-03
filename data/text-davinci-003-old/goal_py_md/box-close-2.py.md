

# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above the lid
    #  2. Pick up the lid with the gripper
    #  3. Place the lid on the box 
    # First, put the gripper above the lid. 
    if check("the robot's gripper is not vertically aligned with the lid"):
        robot.move_gripper("vertically aligned with the lid")
    # Once the gripper is lined up with the lid, close the gripper to grab the lid. 
    if check("the robot's gripper is not around the lid and the robot's gripper is open"):
        robot.move_gripper("around the lid", close_gripper=True)
    # If the lid is in the gripper and the lid is not above the box, move the lid to above the box
    if check("the robot's gripper is around the lid and the lid is not above the box"):
        robot.move_gripper("above the box")
    # Once the lid is above the box, place the lid on the box.  
    if check("the robot's gripper is above the box"):
        robot.move_gripper("near the box")