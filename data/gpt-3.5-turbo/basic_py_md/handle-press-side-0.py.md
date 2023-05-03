# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not almost horizontally aligned with handle"):
        robot.move("gripper to side of handle")
    if check("the robot's gripper is almost horizontally aligned with handle"):
        robot.put("gripper on the side of handle")
    if check("the robot's gripper is on the side of handle and the handle is not pressed"):
        robot.push("down on handle")