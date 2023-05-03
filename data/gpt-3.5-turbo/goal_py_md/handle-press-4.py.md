# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is above the handle, drop it down to grab the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not around the handle"):
        robot.move_gripper("around the handle")
    # Finally, push down on the handle to make it actuate.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("near the ground")