# handle-press: push down the handle
def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle
    #  3. Push handle down
    # This is a simple task, first we should move the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Once the gripper is above the handle, we can grab it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.grab("handle")
    # Now that the gripper is holding onto the handle we can push it down.
    if check("the robot's gripper is around handle"):
        robot.push("down on handle")