

Please start with an explanation of the algorithm you will use. Write one
sentence to describe each step in the algorithm.


"""
def button_press_topdown(robot):
    # Steps:
    #  1. Move the gripper over the button
    #  2. Push the button down
    #  3. Hold the button
    # We don't need to be precise, so just start pushing straight down until the
    # button has been pressed and the gripper is roughly above it.
    if check("the button has not been pressed"):
        robot.push("the button down")
    # Once the gripper is above the button we need to be more careful not to
    # knock the button over while pushing it.
    # We still need to be pushing down, so if the button is in front of the
    # robot's gripper we want to push harder to keep holding the button down.
    if check("the button has been pressed and the robot's gripper is above the button and the button is in front of the robot's gripper"):
        robot.push("the button down")


###############################################################
# Part 3
###############################################################
print("""


""")

def button_press_topdown(robot):
    # Steps:
    #  1. Move the gripper over the button
    #  2. Push the button down
    #  3. Hold the button
    # We don't need to be precise, so just start pushing straight down until the
    # button has been pressed and the gripper is roughly above it.
    if check("the button has not been pressed"):
        robot.push("the button down")
    # Once the gripper is above the button we need to be more careful not to
    # knock the button over while pushing it.
    # We still need to be pushing down, so if the button is in front of the
    # robot's gripper we want to push harder to keep holding the button down.
    if check("the button has been pressed and the robot's gripper is above the button and the button is in front of the robot's gripper"):
        robot.push("the button down")

[eod] [code]
# 900. RLE Iterator


class RLEIterator(object):
    def __init__(self, A):
        