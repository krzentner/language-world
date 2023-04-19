# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put the gripper to the side of the handle
    #  2. Grab the handle with the gripper
    #  3. Push the handle down
    # First, we need to move the robot's gripper to the side of the handle.
    if check("the robot's gripper is not to the side of the handle"):
        robot.move("the gripper to the side of the handle")
    # Once the gripper is to the side of the handle, we can grab the handle.
    if check("the robot's gripper is near the handle and the gripper is not around the handle"):
        robot.grab("the handle with the gripper")
    # Once the handle is grabbed, push it down.
    if check("the gripper is around the handle"):
        robot.push("the handle down")