# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper above the plate
    #  2. Push the plate with the gripper until it reaches the target location
    # First, put the gripper above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    # If the gripper is above the plate, push the plate until it reaches the
    # target location.
    if check("the robot's gripper is above the plate"):
        robot.move_gripper("above the target location")