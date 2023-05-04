
"""

import tensorflow as tf
import numpy as np

_TASK_NAMES = ['peg-insert-side', 'push', 'window-close', 'window-open',
               'button-press-topdown', 'reach', 'pick-place',
               'door-open', 'drawer-open', 'drawer-close', 'dial-turn']
_ROBOT_NAME = 'robot'
_ACTION_DESCRIPTION_LIST = ['left', 'right', 'up', 'down', 'back', 'into', 'out_of',
                            'open', 'closed', 'near', 'at', 'above',
                            'left_of', 'right_of', 'vertically_aligned_with',
                            'horizontally_aligned_with', 'forward_aligned_with']


def get_action_description(robot, action, description):
    name = robot.name
    actions = robot.available_actions
    if description in _ACTION_DESCRIPTION_LIST:
        description_to_action = {
            'left': 'left_turn',
            'right': 'right_turn',
            'up': 'lift',
            'down': 'lower',
            'back': 'backward_move',
            'into': 'grab',
            'out_of': 'release',
            'open': 'open_gripper',
            'closed': 'close_gripper',
            'near': 'approach',
            'at': 'reach',
            'above': 'go_above',
            'left_of': 'go_left',
            'right_of': 'go_right',
            'vertically_aligned_with': 'go_up',
            'horizontally_aligned_with': 'go_right',
            'forward_aligned_with': 'go_right',
        }
        # return action if `name` in `action` else None
        return actions['action'] == actions['action'][0] + '_gripper'
    else:
        return False


def get_object_list(robot, object_list, state, description):
    name = robot.name
    states =