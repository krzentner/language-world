
"""
        return task_desc, lang, "button_press"

    @staticmethod
    def get_task(lang='en'):
        """task-specific params:
            name: `button-press`
        """

        task_desc = """\

# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
"""

        return task_desc, lang, "button_press"


class Drawer_close_task(Robot_task):
    @staticmethod
    def get_prompt(lang='en'):
        """prompt-specific params:
            name: `button-press`
        """
        task_desc = """\

# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
"""
        return task_desc, lang, "button_press"

    @staticmethod
    def get_task(lang='en'):
        """task-specific params:
            name: `button-press`
        """

        task_desc = """\

# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
"""

        return task_desc, lang, "button_press"


class Drawer_open_task(Robot_task):
    @staticmethod
    def get_prompt(lang='en'):
        """prompt-specific params:
            name: `button-press`
        """
        task_desc = """\

# button-press: push the button from the front
def button_press(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is