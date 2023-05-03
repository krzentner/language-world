# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the handle is not in the gripper, grab it.
    if check("the robot's gripper is not around handle and the handle is below the robot's gripper"):
        robot.drop("gripper around handle")
    # Push down on the handle to activate it.
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")