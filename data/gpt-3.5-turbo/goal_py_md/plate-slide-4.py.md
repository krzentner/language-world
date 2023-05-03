# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    #  1. Put gripper near edge of the plate
    #  2. Push the plate
    # We need to position the gripper near the edge of the plate so we can push
    # it.
    if check("the robot's gripper is not near the edge of the plate"):
        robot.move_gripper("near the edge of the plate")
    # Once the gripper is near the edge of the plate, we can push it into the
    # target location.
    if check("the robot's gripper is near the edge of the plate"):
        robot.move_gripper("above the target location")