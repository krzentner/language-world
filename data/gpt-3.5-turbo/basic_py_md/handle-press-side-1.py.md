# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the gripper is not to left of the handle and the gripper is forward of the handle"):
        robot.move("gripper to left of handle")
    if check("the gripper is to the left of the handle and the gripper is not around handle"):
        robot.grab("handle")
    if check("the gripper is around handle and the handle is not pressed down"):
        robot.push("down on handle")