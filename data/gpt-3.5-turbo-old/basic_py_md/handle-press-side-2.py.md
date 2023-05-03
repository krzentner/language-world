# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not forward aligned with the handle and the handle is not left of the robot's gripper"):
        robot.move("gripper to the left of the handle")
    if check("the robot's gripper is forward aligned with the handle and the handle is not horizontally aligned with the base"):
        robot.align("handle to base")
    if check("the gripper is at the handle's height and the handle is not pushed down"):
        robot.push("handle down")