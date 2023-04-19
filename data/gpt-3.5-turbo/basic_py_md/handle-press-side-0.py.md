# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to the left of the handle")
    if check("the robot's gripper is above the handle"):
        robot.move("gripper to the center of the handle")
    if check("the robot's gripper is around the handle"):
        robot.close("gripper around handle")
    if check("the robot's gripper is holding the handle"):
        robot.push("down on the handle")