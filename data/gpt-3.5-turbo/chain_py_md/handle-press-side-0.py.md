# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper around handle
    #  2. Push down on handle from the side
    # First, put the gripper around the handle.
    if check("the robot's gripper is not around handle"):
        robot.grab("handle")
    # If the robot's gripper is not to the side of the handle, move it there.
    # Because the handle is long, check for horizontal alignment with the
    # gripper instead of just overlap.
    if check("handle is not vertically aligned with the robot's gripper and handle is not to the side of the robot's gripper"):
        robot.move("gripper to handle side")
    # Once the gripper is to the side of the handle, push down on the handle.
    if check("the robot's gripper is to the side of the handle"):
        robot.push("down on handle from the side")