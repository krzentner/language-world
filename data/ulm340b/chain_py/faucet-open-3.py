
    # Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the faucet handle left
    # As long as the robot's gripper is still not around the faucet handle, we
    # keep trying to put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Now that the gripper is around the faucet handle, we can try turning the
    # faucet handle left.
    if check("the robot's gripper is around faucet handle and the robot's gripper is horizontally aligned with faucet handle"):
        robot.turn("faucet handle left")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around the faucet handle
    #  2. Turn the faucet handle right
    # As long as the robot's gripper is still not around the faucet handle, we
    # keep trying to put the gripper around the faucet handle.
    if check("the robot's gripper is not around the faucet handle"):
        robot.grab("faucet handle")
    # Now that the gripper is around the faucet handle, we can try turning the
    # faucet handle right.
    if check("the robot's gripper is around faucet handle and the robot's gripper is horizontally aligned with faucet handle"):
        robot.turn("faucet handle right")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
    #  1. Put gripper next to the button
    #  2. Push down on the button from the side
    # This time we'll push down on the button by pushing sideways on it.
    # First, we put the gripper next to the button.
    if check("the robot's gripper is not left of button"):
        robot.put("gripper left of button")
    # Now that the gripper is to the left of the button, push down on the button
    # from the side.
    if check("the robot's gripper is left of button"):
        robot.push("down on button")

# button-press-bottom: push the button from below
def button_press_bottom(robot