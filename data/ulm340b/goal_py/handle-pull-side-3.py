
    # Steps:
    #  1. Put the gripper on top of the handle
    #  2. Slide the handle open
    # First, we need to put the gripper on top of the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is on top of the handle, we can pull it open.
    if check("the robot's gripper is above the handle and the robot's gripper is not horizontally aligned with the handle"):
        robot.move_gripper("around the handle")
    # If the gripper is above the handle, move it up to make the handle open.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("near the handle")

# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Put gripper on top of the handle
    #  2. Slide the handle open
    # First, we need to put the gripper on top of the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is on top of the handle, we can pull it open.
    if check("the robot's gripper is above the handle and the robot's gripper is not forward aligned with the handle"):
        robot.move_gripper("around the handle")
    # If the gripper is above the handle, move it up to make the handle open.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("near the handle")

# bottle-open: open the bottle by twisting off the cap
def bottle_open(robot):
    # Steps:
    #  1. Put gripper on top of the cap
    #  2. Put gripper around the cap
    #  3. Move the cap to twist it off
    # First, we need to put the gripper on top of the cap.
    if check("the robot's gripper is not above the cap"):
        robot.move_gripper("vertically aligned with the cap")
    # Once the gripper is on top of the cap,