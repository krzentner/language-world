
    # Steps:
    #  1. Put gripper right above plate
    #  2. Move gripper left to slide plate
    #  3. Slide the plate until it is lined up with the target location
    # First, put the gripper right above the plate.
    if check("the robot's gripper is not above plate"):
        robot.move_gripper("above the plate")
    # Once the gripper is above the plate, start sliding it by moving the
    # gripper to the left.
    if check("the robot's gripper is above the plate and the robot's gripper is not left of the plate"):
        robot.move_gripper("left of the plate")
    # Once the gripper is near the plate, move it until the plate is lined up
    # with the target location.
    if check("the plate is horizontally aligned with target"):
        robot.move_gripper("above the plate")

# plate-push: push the plate into the target location
def plate_push(robot):
    # Steps:
    #  1. Put gripper in front of plate
    #  2. Push plate to target location
    # First, put the gripper in front of the plate.
    if check("the robot's gripper is not forward aligned with plate"):
        robot.move_gripper("forward aligned with the plate")
    # If the gripper is in front of the plate, we can start to push it to the
    # target location.
    if check("the robot's gripper is forward aligned with plate"):
        robot.move_gripper("forward aligned with the target location")