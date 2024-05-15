# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # Now that the gripper is lined up, just push down on the handle.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")