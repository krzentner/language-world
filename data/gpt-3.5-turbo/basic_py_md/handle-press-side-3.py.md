# handle-press-side: push down the handle from the side
# def handle_press_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move("gripper to the side of the handle")
        robot.move("gripper above the handle")
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.grab("the handle")
    if check("the robot's gripper is around the handle and the handle is not pressed down"):
        robot.push("down on the handle")