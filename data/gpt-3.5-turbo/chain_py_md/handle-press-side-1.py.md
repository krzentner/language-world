# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Position gripper next to handle on the side
    #  2. Push gripper down to press handle
    # First, position the gripper next to the handle on the side.
    if check("the robot's gripper is not next to the handle"):
        robot.move("gripper to the side of handle")
    # Once the gripper is next to the handle, push it down to press the handle.
    if check("the robot's gripper is next to the handle"):
        robot.push("down on handle")