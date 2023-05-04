

Your robot program should perform the following steps in order:

1. Put gripper around the handle.
2. Drop gripper down below the handle.
3. Close the gripper around the handle.
4. Push the handle down.

For example, if your robot program contains the statements `robot.move_gripper("around the handle")`,
`robot.move_gripper("below the handle")`,
and `robot.move_gripper("almost aligned with the handle", close_gripper=True)`
in the correct order, you will earn a point.
"""
from . import (
    generate_robot,
    setup_robot,
)


def generate_random_goal():
    task_names = [
        "door-open",
        "drawer-open",
        "button-press-topdown",
        "drawer-close",
        "push",
        "window-close",
        "window-open",
        "reach",
        "pick-place",
        "door-open",
    ]
    return task_names[generate_robot.random.randrange(len(task_names))]


def generate_goal_name():
    task_names = [
        "door-open",
        "drawer-open",
        "button-press-topdown",
        "drawer-close",
        "push",
        "window-close",
        "window-open",
        "reach",
        "pick-place",
        "door-open",
    ]
    goal_name = generate_robot.random.choice(task_names)
    return goal_name


def handle_press(robot):
    # Steps:
    #  1. Put gripper around the handle.
    #  2. Drop gripper down below the handle.
    #  3. Close the gripper around the handle.
    #  4. Push the handle down.

    # First, put the gripper around the handle.
    if check("the robot's gripper is not almost aligned with the handle"):
        robot.move_gripper("around the handle", close_gripper=True)

    # If the gripper is around the handle, drop it down below the handle.
    # Because the handle is a long object, make sure the gripper is not just
    # above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_g