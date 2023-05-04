

Now write the program. Your program must not be longer than 13 lines.

"""


task_template = """
# {task_description}
def {task_name}(robot):
    {program_lines}
"""

solution_template = """
# {task_description}
def {task_name}(robot):
    if check("{cond_1}"):
        robot.place("{cond_1}")
    if check("{cond_2}"):
        robot.place("{cond_2}")
    if check("{cond_3}"):
        robot.place("{cond_3}")
"""

task_types = [
    "push",
    "pick-place",
    "drawer-close",
    "drawer-open",
    "window-open",
    "window-close",
    "door-open",
    "button-press-topdown",
    "peg-insert-side"
]

program_dict = {
    "button-press-topdown":
        """
        # button-press-topdown: push the button down from above
        def button_press_topdown(robot):
            if check("the robot's gripper is not vertically aligned with button"):
                robot.put("gripper above button")
            if check("the robot's gripper is vertically aligned with button"):
                robot.push("down on button")
        """,
    "door-open":
        """
        # door-open: pull the door open
        def door_open(robot):
            if check("the robot's gripper is not almost vertically aligned with door handle"):
                robot.put("gripper above door handle")
            if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
                robot.put("gripper around door handle")
            if check("the robot's gripper is vertically aligned with the door handle"):
                robot.pull("door open")
        """,
    "window-close":
        """
        # window-close: slide the window closed to the right
        def window_close(robot):
            if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
                robot.move("gripper to left of window handle")
            if check("the robot's gripper is near the window handle"):
                robot.slide("window right")
            if check("the robot's gripper is in front of the window handle"):
