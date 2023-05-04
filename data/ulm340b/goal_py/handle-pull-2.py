
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.move_gripper("almost vertically aligned with the handle")
    # As long as the gripper is mostly aligned, we can just go grab the handle.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not near handle"):
        robot.move_gripper("around the handle")
    # If we have the handle, we should be able to pull it up now.
    if check("the robot's gripper is around handle and the robot's gripper is open"):
        robot.move_gripper("above the handle")

# handle-pull-side: pull the handle up from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not above handle"):
        robot.move_gripper("almost vertically aligned with the handle")
    # As long as the gripper is mostly aligned, we can just go grab the handle.
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle", close_gripper=True)
    # If we have the handle, we should be able to pull it up now.
    if check("the robot's gripper is around handle and the robot's gripper is open"):
        robot.move_gripper("above the handle", close_gripper=True)

# handle-turn: rotate the handle
def handle_turn(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Turn the handle
    # First, put the gripper mostly above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move