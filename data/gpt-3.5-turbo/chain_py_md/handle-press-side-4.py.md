# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper beside the handle
    #  2. Push down on the handle from the side
    # First, move the gripper beside the handle.
    if check("the robot's gripper is not beside the handle"):
        robot.move("gripper beside the handle")
    # If the gripper is beside the handle, push down on the handle from the side.
    if check("the robot's gripper is beside the handle"):
        robot.push("down on handle from the side")