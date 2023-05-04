

"""
# TODO: Add the main block of your code here
drawer_open_steps = [
    "the robot's gripper is not right of the drawer handle",
    "the robot's gripper is forward aligned with drawer handle and the robot's gripper is not almost vertically aligned with the drawer handle",
    "the robot's gripper is almost vertically aligned with the drawer handle",
]


def drawer_open(robot):
    if check(drawer_open_steps[0]):
        robot.move_gripper("near the drawer handle", close_gripper=True)
    elif check(drawer_open_steps[1]):
        robot.move_gripper("vertically aligned with the drawer handle")
    elif check(drawer_open_steps[2]):
        robot.move_gripper("left of the drawer handle", close_gripper=True)


"""
Now let's test your code, starting with the `reach` task.
We can run the code to see how the robot will perform the task:

"""


def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.move_gripper("near the reach target")


run_robot(reach)


"""
You can see that your robot is not yet doing the right thing. Try to modify
the code until the robot performs the task correctly.

The robot should be able to perform the `reach` task:

"""

run_robot(reach)

"""
Good! Now that you know how to run the robot, you can finish programming it
so it can complete the rest of the tasks.

The tasks are: `drawer-close`, `drawer-open`, `button-press-topdown`,
`door-open`, `door-close`, `pick-place`, `push`, `reach`, `window-close`,
`window-open`.

The robot should be able to perform the `window-close` task:

"""

run_robot(window_close)

"""
Good! Now that you know how to run the robot, you can finish programming it
so it can complete the rest of the tasks.

The tasks are: `drawer-close`, `drawer-open`, `button-press-topdown`,
`door-open`, `door-close`, `pick-place`, `push`, `reach`, `window-close`,
`window-open`.

The robot should be able to perform the `button-press-topdown` task:

"""

run_robot(button_press_top