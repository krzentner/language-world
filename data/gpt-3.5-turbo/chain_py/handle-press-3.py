# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # Once the gripper is above the handle, drop it around the handle.
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, push down on the handle.
    if check("the robot's gripper is around the handle"):
        robot.push("down on the handle")