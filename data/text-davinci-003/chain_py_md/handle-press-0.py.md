

# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Push down the handle
    # Put the robot's gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the gripper is vertically aligned with the handle, push down on it.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on handle")