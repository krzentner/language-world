# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle
    #  3. Push down on the handle
    # Begin by putting the gripper above the handle
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move("the gripper above the handle")
    # Once the gripper is above the handle, grab the handle
    if check("the robot's gripper is vertically aligned with the handle and the gripper is open"):
        robot.grab("the handle")
    # Push down on the handle to activate it
    if check("the robot's gripper is holding the handle"):
        robot.push("down on the handle")