
    # Steps:
    #  1. Put gripper roughly above the handle
    #  2. Put gripper above the handle
    #  3. Drop gripper around the handle
    #  4. Move the gripper up
    # First, put the gripper roughly above the handle so that we don't bump the
    # handle while trying to grab it.
    if check("the robot's gripper is not above handle"):
        robot.move_gripper("almost vertically aligned with the handle")
    # If the gripper is almost above the handle, put it exactly above the handle.
    if check("the robot's gripper is above handle and the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Once the gripper is above the handle, we should be able to put the gripper
    # around the handle by moving it down.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # Once the gripper is around the handle, we should be able to pull the handle
    # up by moving the gripper up.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.move_gripper("above the handle", close_gripper=True)

# handle-slide: slide the handle to the left
def handle_slide(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Put gripper almost above the handle
    #  3. Drop gripper around the handle
    #  4. Push the handle left
    # First, put the gripper roughly above the handle so that we don't bump the
    # handle while trying to grab it.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.move_gripper("almost vertically aligned with the handle", close_gripper=True)
    # If the gripper is almost above the handle, put it exactly above the handle.
    if check("the robot's gripper is almost vertically aligned with handle and the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")