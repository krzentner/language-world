# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper around the handle from the side
    #  2. Push down on the handle
    # First, position the gripper around the handle from the side.
    if check("the robot's gripper is not around the handle and the handle is not vertically aligned with the robot's gripper"):
        robot.move("gripper to side of handle")
        robot.drop("gripper around handle")
    # Once the gripper is around the handle, push down on the handle to activate it.
    if check("the robot's gripper is around the handle and the handle is vertically aligned with the robot's gripper"):
        robot.push("down on handle")