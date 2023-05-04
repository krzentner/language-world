
'''
task_desc = '''
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    pass
'''
task = '''
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper above the lid
    #  2. Lower gripper around lid
    #  3. Grasp lid
    #  4. Put gripper above box
    #  5. Lower gripper to drop the lid
    # Put gripper above the box lid.
    if check("the robot's gripper is not above the lid"):
        robot.move_gripper("above the lid", close_gripper=True)
    # Drop the gripper to grab the lid.
    if check("the robot's gripper is not around the lid"):
        robot.move_gripper("near the lid")
    # Now that the gripper is around the lid, lift it by closing the gripper.
    if check("the robot's gripper is around the lid and the robot's gripper is open"):
        robot.move_gripper("vertically aligned with the lid", close_gripper=True)
    # Put gripper above box.
    if check("the robot's gripper is not above the box"):
        robot.move_gripper("above the box", close_gripper=True)
    # Drop the lid onto the box.
    if check("the robot's gripper is not above the box"):
        robot.move_gripper("near the box")
'''
task_no_comments = '''
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper above the lid
    #  2. Lower gripper around lid
    #  3. Grasp lid
    #  4. Put gripper above box
    #  5. Lower gripper to drop the lid
    if check("the robot's gripper is not above the lid"):
        robot.move_gripper("above the lid", close_gripper=True)
    if check("the robot's gripper is not around the lid"):
        robot.move_gripper("near