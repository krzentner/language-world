# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push the gripper down onto the plate
    #  3. Slide the plate into the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate then push the gripper down onto the
    # plate.
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is near the plate then slide the plate into the target
    # location.
    if check("the robot's gripper is near the plate and the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")