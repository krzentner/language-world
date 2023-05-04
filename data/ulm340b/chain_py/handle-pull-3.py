
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull the handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # As long as the gripper is above the handle, it's ok to put the gripper
    # around the handle.
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    # Now that the gripper is around the handle, we can pull it.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")

# handle-press: press the handle in
def handle_press(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Press the handle down
    # First, line up the gripper with the handle.
    # Because the handle is wide, we don't need to be that accurate, but we do
    # need to put it above the handle.
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # As long as the gripper is above the handle, it's ok to push the handle
    # down.
    if check("the robot's gripper is above handle"):
        robot.push("the handle down")

# handle-slide: slide the handle to the side
def handle_slide(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Put gripper around handle
    #  3. Slide handle to the side
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above handle"):
        robot.put("gripper above handle")
    # As long as the gripper is above the handle, it's ok to put the gripper
    # around the handle.
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.put("gripper around handle")
