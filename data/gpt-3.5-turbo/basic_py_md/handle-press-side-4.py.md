# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    if check("the robot's gripper is forward aligned with the handle and the handle is not horizontally aligned with the target"):
        robot.align("handle to target")
    if check("the handle is horizontally aligned with the target"):
        robot.push("down on handle")