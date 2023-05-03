# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Move the gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Move the gripper to the side of the handle
    #  4. Pull the handle up
    # Move the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is above the handle, close the gripper around the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # After gripping the handle, move the gripper to the side of the handle.
    if check("the robot's gripper is around the handle and the robot's gripper is not left of the handle"):
        robot.move_gripper("left of the handle")
    # Once the gripper is to the side of the handle, pull the handle up.
    if check("the robot's gripper is left of the handle"):
        robot.move_gripper("above the handle")