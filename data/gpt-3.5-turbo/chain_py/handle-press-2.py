# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Grab handle with gripper
    #  2. Push down on the handle
    # First, position the gripper correctly by moving it near the handle.
    # Since we don't need to be precise about the position, we can just move it
    # to the middle between the handle and whatever is surrounding it.
    if check("the robot's gripper is not near the handle"):
        robot.move("gripper near handle")
    # Once the gripper is near the handle, grab the handle.
    if check("the robot's gripper is near the handle and the robot's gripper is open"):
        robot.grab("handle")
    # Finally, push down on the handle to activate it.
    if check("the robot's gripper is around the handle"):
        robot.push("down on handle")