
    # Steps:
    #  1. Line up the gripper
    #  2. Push the button in from above
    # Because the button is blocked by a wall, we have to approach it from the
    # side.
    # Line up the gripper with the button.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper with button")
    # We don't know if the button is below the gripper, but we should push down
    # in any case, and this will make the button go in.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on the button")

# button-press-side: push the button in from the front
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper
    #  2. Push the button in from above
    # Because the button is not blocked, we can just push it in from the front.
    # Line up the gripper with the button.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.align("gripper with button")
    # We don't know if the button is below the gripper, but we should push down
    # in any case, and this will make the button go in.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("down on the button")

# valve-turn-side: turn the valve from the front
def valve_turn_side(robot):
    # Steps:
    #  1. Line up the gripper
    #  2. Push the valve in from the top
    #  3. Turn the valve
    # We can approach the valve from the front.
    # Line up the gripper with the valve.
    if check("the robot's gripper is not horizontally aligned with valve"):
        robot.align("gripper with valve")
    # We don't know if the valve is below the gripper, but we should push down
    # in any case, and this will make the valve go in.
    if check("the robot's gripper is horizontally aligned with valve"):
        robot.push("down on the valve")
    # The valve