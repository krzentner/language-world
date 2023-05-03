# handle-pull: pull up the handle
def handle_pull(robot):
    # Steps:
    #   1. Move the gripper above the handle
    #   2. Close the gripper around the handle
    #   3. Lift the handle upwards
    # First, move the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # Once the gripper is above the handle, close it to grab the handle.
    if check("the robot's gripper is above the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # Once we've grabbed the handle, lift it upwards.
    if check("the robot's gripper is around handle"):
        robot.pull("handle upwards")