# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    if check("the robot's gripper is not aligned with the handle and the gripper is not near the handle"):
        robot.move("gripper to side of the handle")
    if check("the robot's gripper is near the handle and the gripper is not vertically aligned with the handle"):
        robot.move("gripper up to handle")
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.push("down on handle")