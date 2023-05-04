

'''
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into side of plate
    #  3. Slide plate into the target location
    # The robot can slide the plate by trapping it by pushing against it from the side and moving the gripper.
    # If the plate isn't in front of the gripper as seen from above, move the gripper to above the plate.
    if check("the plate is not in front of the robot's gripper"):
        robot.move_gripper("forward aligned with plate")
    # If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.
    if check("the plate is in front of the robot's gripper and the plate is not near the robot's gripper"):
        robot.move_gripper("almost aligned with plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can slide it to the target location.
    if check("the plate is near the robot's gripper and the plate is in front of the robot's gripper"):
        robot.move_gripper("above the target location")
'''
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper above plate
    #  2. Push gripper into side of plate
    #  3. Slide plate into the target location
    # The robot can slide the plate by trapping it by pushing against it from the side and moving the gripper.
    # If the plate isn't in front of the gripper as seen from above, move the gripper to above the plate.
    if check("the plate is not in front of the robot's gripper"):
        robot.move_gripper("forward aligned with plate")
    # If the gripper is aligned with the plate but not near it, move the gripper down to the plate to slide it.
    if check("the plate is in front of the robot's gripper and the plate is not near the robot's gripper"):
        robot.move_gripper("almost aligned with plate", close_gripper=True)
    # If the gripper is near the plate, we've probably trapped the plate and can slide it to the target location.
    if check("