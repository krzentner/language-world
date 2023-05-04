
'''

coffee_button_task = '''
# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # First we need to get the gripper into position above the button
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")

    # Now the button is aligned with the gripper, so we need to push on it
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
'''

# coffee_button_solution = '''
# coffee-button: push the button on the coffee machine
# Steps:
#   1. Put gripper above the button
#   2. Push gripper down on button
# First, put the gripper above the button so that we can push it straight down.
if check("the robot's gripper is not vertically aligned with button"):
    robot.put("gripper above button")
# Now that the gripper is lined up, just push down on the button.
if check("the robot's gripper is vertically aligned with button"):
    robot.push("down on button")
# '''

button_press_side = '''
# button-press-side: push the button sideways
def button_press_side(robot):
    # First we need to get the gripper into position in front of the button
    if check("the robot's gripper is not forward aligned with button"):
        robot.put("gripper in front of button")

    # Now the button is aligned with the gripper, so we need to push on it
    if check("the robot's gripper is forward aligned with button"):
        robot.push("button from the side")
'''

tasks = {
    'reach': 'reach',
    'window-close': 'window-close',
    'drawer-open': 'drawer-open',
    'peg-insert-side': 'peg-insert-side',
    'push': 'push',
    'door-open': 'door-open',
    'pick-place': 'pick-place',
    'window-open': 'window-open',
    'drawer-close': 'drawer-close',
    'button-press-topdown': 'button-press-topdown',
}

coffee_button_task = '''