
""")

    assert check_function_definition_exists(handle_pull_side_name)


def test_handle_pull_side_1(execute_program_in_buffer):
    execute_program_in_buffer(handle_pull_side_name, handle_pull_side_code, """
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up the handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    # If the gripper is almost around the handle, close it to grab the handle.
    if check("the robot's gripper is almost around handle and the robot's gripper is open"):
        robot.close("around handle")
    # As long the gripper is around the handle, pull up the handle.
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")
    """)

    assert check_function_definition_exists(handle_pull_side_name)


@pytest.mark.timeout(30)
def test_handle_pull_side_2(execute_program_in_buffer):
    execute_program_in_buffer(handle_pull_side_name, handle_pull_side_code, """
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Pull up the handle
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is almost around handle and the robot's gripper is open"):
        robot.close("around handle")
    if check("the robot's gripper is around handle"):
        robot.pull("handle up")
    """)

    assert check_function_definition_exists(handle_pull_side_name)
[eod] [code]import os
import shutil


def mkdir(d):
    '''