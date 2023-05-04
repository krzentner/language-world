
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Close gripper around the mug handle
    #  3. Move the mug to the target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle", close_gripper=True)
    # If the gripper is around the mug handle, we can move the mug by moving the
    # gripper.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("left of the target location")

# coffee-push: grab the mug and push it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug handle
    #  2. Close gripper around the mug handle
    #  3. Move the mug to the target location
    # First, put the gripper above the mug handle.
    if check("the robot's gripper is not above the mug handle"):
        robot.move_gripper("above the mug handle", close_gripper=True)
    # If the gripper is around the mug handle, we can move the mug by moving the
    # gripper.
    if check("the robot's gripper is around the mug handle"):
        robot.move_gripper("right of the target location")

# coffee-open: twist open the lid of the coffee mug
def coffee_open(robot):
    # Steps:
    #  1. Put gripper above the lid
    #  2. Grab lid with gripper
    #  3. Twist lid open
    # First, put the gripper above the lid.
    if check("the robot's gripper is not above the lid"):
        robot.move_gripper("vertically aligned with the lid", close_gripper=True)
    # If the gripper is not right of the lid, then maybe we can grab it.
    # This means the gripper will be right of the lid.
    if check("the robot's gripper is not right of the lid"):
        robot.move_gripper("horizontally aligned with the lid")
    # If the gripper is right