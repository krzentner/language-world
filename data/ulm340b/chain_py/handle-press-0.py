
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab the handle
    #  3. Push the handle down
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.place("gripper above handle")
    # If the gripper is above the handle but not around it, put the gripper
    # around the handle.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    # If the gripper is around the handle but above it, push the gripper down.
    if check("the robot's gripper is around handle and the robot's gripper is vertically aligned with handle"):
        robot.press("handle down")

# handle-pull: pull the handle up
def handle_pull(robot):
    # Steps:
    #  1. Put gripper below handle
    #  2. Grab the handle
    #  3. Pull the handle up
    # First, put the gripper roughly below the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.place("gripper below handle")
    # If the gripper is below the handle but not around it, put the gripper
    # around the handle.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    # If the gripper is around the handle but below it, pull the gripper up.
    if check("the robot's gripper is around handle and the robot's gripper is vertically aligned with handle"):
        robot.pull("handle up")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper as viewed from in front
    #  2. Push sideways on the button
    # Because this is "side", we need to line up the gripper from in front.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not forward aligned with button"):
