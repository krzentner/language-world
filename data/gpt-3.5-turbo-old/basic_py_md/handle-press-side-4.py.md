# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is to the right of the handle"):
        robot.move("the gripper to the left of the handle")
    if check("the robot's gripper is to the left of the handle"):
        robot.put("the gripper around the handle")
    if check("the robot's gripper is around the handle and the handle is not pushed down"):
        robot.push("down on handle")