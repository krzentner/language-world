# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    # 1. Put gripper next to handle
    # 2. Grab the handle with the gripper
    # 3. Push down on the handle
    # 4. Release the handle
    # First, put the gripper next to the handle.
    if check("the robot's gripper is not next to the handle"):
        robot.move("gripper to the side of the handle")
    # If the gripper is next to the handle, we can try to grab it.
    if check("the robot's gripper is next to the handle"):
        robot.grab("the handle")
    # As long as the gripper is around the handle, press down on it.
    if check("the robot's gripper is around the handle"):
        robot.push("down on the handle")
    # If the gripper is still around the handle, release it.
    if check("the robot's gripper is closed around the handle"):
        robot.release("the handle")