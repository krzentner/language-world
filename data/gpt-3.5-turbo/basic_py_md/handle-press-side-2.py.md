# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the gripper is not beside the handle"):
        robot.move("gripper beside handle")
    if check("the robot's gripper is beside the handle"):
        robot.put("gripper on handle")
    if check("the robot's gripper is on the handle"):
        robot.push("down on the handle")