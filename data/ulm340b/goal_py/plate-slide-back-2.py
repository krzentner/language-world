
    # Steps:
    #  1. Line up the gripper behind the plate
    #  2. Close the gripper on the front of the plate
    #  3. Push the plate back
    # First, put the gripper behind the plate.
    if check("the robot's gripper is not behind plate"):
        robot.move_gripper("behind plate")
    # If the gripper is behind the plate but not close to it, move it forward.
    # We'll push it back after we can grab the front of the plate.
    if check("the robot's gripper is behind plate and the robot's gripper is not almost aligned with plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is aligned with the plate, we can probably push it to the
    # target location.
    if check("the robot's gripper is aligned with plate"):
        robot.move_gripper("aligned with plate")

# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Line up the gripper with the plate to the side
    #  2. Close the gripper on the side of the plate
    #  3. Push the plate sideways
    # First, put the gripper to the side of the plate.
    if check("the robot's gripper is not to the side of plate"):
        robot.move_gripper("to the side of plate")
    # If the gripper is to the side of the plate but not close to it, move it
    # sideways.
    # We'll push it sideways after we can grab the side of the plate.
    if check("the robot's gripper is to the side of plate and the robot's gripper is not almost aligned with plate"):
        robot.move_gripper("near the plate", close_gripper=True)
    # If the gripper is aligned with the plate, we can probably push it to the
    # target location.
    if check("the robot's gripper is aligned with plate"):
        robot.move_gripper("aligned with plate")

# block-push-topdown: push the block in the direction of the goal by pushing from the top
def block_push_topdown