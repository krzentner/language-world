
"""


class Explanations(object):
    @staticmethod
    def task_to_str(task):
        return Explanations.task_to_str_[task]

    @staticmethod
    def robot_to_str(robot):
        return robot.name

    @staticmethod
    def get_instruction(task, robot, step):
        return Explanations.robot_to_str(robot) + " " + Explanations.task_to_str(task) + " " + Explanations.step_to_str(step)

    @staticmethod
    def get_explanation(task, step, step_instruction):
        explanation_dict = {
            'button-press-topdown': Explanations.button_press_topdown,
            'button-press-side': Explanations.button_press_side,
            'drawer-close': Explanations.drawer_close,
            'drawer-open': Explanations.drawer_open,
            'door-lock': Explanations.door_lock,
            'door-unlock': Explanations.door_unlock,
            'hammer': Explanations.hammer,
            'pick-out-of-hole': Explanations.pick_out_of_hole,
            'pick-place': Explanations.pick_place,
            'peg-insert-side': Explanations.peg_insert_side,
            'push': Explanations.push,
            'window-close': Explanations.window_close,
            'window-open': Explanations.window_open
        }
        return explanation_dict[task][step]

    @staticmethod
    def task_to_str_(task):
        return {
            'button-press-topdown': 'push the button down from above',
            'button-press-side': 'push the button with the gripper from the side',
            'drawer-close': 'push the drawer close',
            'drawer-open': 'pull the drawer open',
            'door-lock': 'turn the door lock key clockwise',
            'door-unlock': 'turn the door lock key counterclockwise',
            'hammer': 'hit the nail with the hammer',
            'pick-out-of-hole': 'pull the peg out of the hole',
            'pick-place': 'pick up the puck and hold it at the target location',
            'peg-insert-side': 'grab the peg and insert it into