# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Push down on the handle
    # Position the gripper above the handle
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # Push down on the handle
    if check("the robot's gripper is above the handle"):
        robot.push("down on handle")