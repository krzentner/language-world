# handle-press: push down the handle
# def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push down on handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, push down on the handle by closing the gripper.
    if check("the robot's gripper is near handle and the robot's gripper is open"):
        robot.push("down on handle")