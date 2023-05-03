# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is to the side of the handle and the robot's gripper is not almost vertically aligned with the handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")