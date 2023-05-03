# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper around the handle
    #  2. Push down on the handle
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around the handle"):
        robot.grab("handle")
    # Once the gripper is around the handle, push down on the handle.
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")