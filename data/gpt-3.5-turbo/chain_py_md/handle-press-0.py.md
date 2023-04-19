# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab the handle with the gripper
    #  3. Push down on the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # If the handle becomes left of the gripper, go back to putting the gripper
    # above the handle.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # Once the gripper is holding the handle, push down on it in order to actuate
    # whatever mechanism the handle controls.
    if check("the robot's gripper is holding the handle"):
        robot.push("down on the handle")