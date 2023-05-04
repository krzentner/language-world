
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull handle open
    # First, put the gripper roughly above the handle, so that we can grab it.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.move_gripper("above the handle")
    # Once the gripper is above the handle, drop the gripper around the handle.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move_gripper("around the handle")
    # Finally, pull the handle open by pulling up on the handle.
    if check("the robot's gripper is above handle and the robot's gripper is around handle"):
        robot.move_gripper("above the handle")

# knob-pull: pull the knob open
def knob_pull(robot):
    # Steps:
    #  1. Put gripper above the knob
    #  2. Drop gripper around the knob
    #  3. Pull the knob open
    # First, put the gripper roughly above the knob, so that we can grab it.
    if check("the robot's gripper is not vertically aligned with knob"):
        robot.move_gripper("almost vertically aligned with the knob")
    # Once the gripper is above the knob, drop the gripper around the knob.
    if check("the robot's gripper is vertically aligned with knob and the robot's gripper is not around knob"):
        robot.move_gripper("around the knob")
    # Once the gripper is around the knob, we can pull it open.
    if check("the robot's gripper is above knob and the robot's gripper is around knob"):
        robot.move_gripper("above the knob")


task_funcs = {
    "peg-insert": peg_insert,
    "peg-insert-side": peg_insert_side,
    "peg-unplug": peg_unplug,
    "push": push,
    "reach": reach,
    "window-close": window_close,
    "window-open": window_open,
    "button-press-topdown": button_press_topdown,
    "pick-place": pick_place,
    "