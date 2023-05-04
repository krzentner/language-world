

"""

button_press_topdown_wall_str = """# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Move above the wall
    #  3. Push down on the button from the top
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
"""

# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    """Steps:
    1. Line up the gripper as viewed from above
    2. Move above the wall
    3. Push down on the button from the top
    """
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

"""
# door-open-wall: pull open the door with a small wall in the way
def door_open_wall(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with door handle"):
        robot.grab("door handle")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot