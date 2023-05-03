# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper near the handle
    #  2. Grab the handle with the gripper
    #  3. Push down on the handle
    # First, put the gripper near the handle.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper near handle")
    # If the gripper isn't around the handle, put it around the handle.
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    # If the gripper is near the handle and open, close it to grab the handle.
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.close("gripper around handle")
    # Once the gripper is closed around the handle, push down to press it.
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")