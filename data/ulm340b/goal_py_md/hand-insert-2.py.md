
"""
    return """
# hand-insert: pick up the puck and move it to the target location
def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("near the target location")
"""


def execute_code(code_to_execute):
    """Executes Python code containing a `robot` object to control a robot.

    Please write your code into the following function.
    """
    def execute_code(code_to_execute):
        raise NotImplementedError()
    return execute_code(code_to_execute)


def test_function_exists():
    assert callable(control_robot)


def test_function_type():
    assert (
        isinstance(control_robot(), str)
        or isinstance(control_robot(), list)
        or isinstance(control_robot(), tuple)
    )


def test_function_content():
    expected = """
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):