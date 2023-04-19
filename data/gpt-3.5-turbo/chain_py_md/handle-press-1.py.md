# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Pull gripper around handle
    #  3. Press down on the handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not roughly above handle"):
        robot.place("gripper above handle")
    # If the gripper is not around the handle, move the gripper down around it.
    if check("the robot's gripper is not around handle"):
        robot.pull("gripper around handle")
    # Once the gripper is around the handle, press down on it.
    # Keep applying pressure until we detect that the handle has been pressed down.
    # We use the "check" function to make sure that the handle is being successfully
    # pressed down.
    while check("the handle is not pressed down"):
        robot.push("down on handle")
    print("Handle has been pressed down successfully!")