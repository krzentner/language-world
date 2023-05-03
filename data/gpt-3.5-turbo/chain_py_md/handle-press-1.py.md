# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper around handle
    #  2. Push down on handle
    # The first step is to move the gripper around the handle.
    if check("the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    # Once the gripper is around the handle, push down on the handle.
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")