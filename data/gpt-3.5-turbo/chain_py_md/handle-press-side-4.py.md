# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    # Steps:
    #  1. Put gripper beside the handle
    #  2. Turn gripper to face handle
    #  3. Push down on handle
    # First, move the gripper to the side of the handle
    if check("the robot's gripper is not beside the handle"):
        robot.move("gripper beside the handle")
    # If the gripper is not facing the handle, turn it to face the handle
    if check("the robot's gripper is not facing the handle"):
        robot.turn("gripper to face the handle")
    # Now that the gripper is facing the handle, push down on the handle
    if check("the robot's gripper is facing the handle"):
        robot.push("down on handle")