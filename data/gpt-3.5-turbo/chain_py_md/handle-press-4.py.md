# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # Once the gripper is lined up with the handle, we can simply push down on it.
    # As long as the gripper is still above the handle and not pushing,
    # keep pushing down.
    while check("the robot's gripper is above the handle and the robot's gripper is not pushing down on the handle"):
        robot.push("down on handle")