# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #  1. Move gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull handle upwards
    # To start, move the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Once the gripper is mostly above the handle, it can be dropped around the handle.
    if check("the robot's gripper is almost vertically aligned with handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, pull the handle upwards
    if check("the robot's gripper is around handle"):
        robot.pull("handle upwards")