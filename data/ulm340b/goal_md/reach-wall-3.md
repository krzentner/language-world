
"""

def robot_instruction(task_instruction_1, task_instruction_2):
    instructions = {
        'drawer-open': (task_instruction_1, 'move robot\'s gripper until the robot\'s gripper is around the drawer handle'),
        'window-open': (task_instruction_2, 'move robot\'s gripper until the robot\'s gripper is vertically aligned with the window handle'),
        'door-open': (task_instruction_1, 'move robot\'s gripper until the robot\'s gripper is around the door handle'),
        'window-close': (task_instruction_2, 'move robot\'s gripper until the robot\'s gripper is around the window handle'),
        'drawer-close': (task_instruction_2, 'move robot\'s gripper until the robot\'s gripper is around the drawer handle'),
        'peg-insert-side': (task_instruction_1, 'move robot\'s gripper until the robot\'s gripper is horizontally aligned with hole'),
        'button-press-topdown': (task_instruction_2, 'move robot\'s gripper until the robot\'s gripper is near the button'),
        'pick-place': (task_instruction_2, 'move robot\'s gripper until the robot\'s gripper is near the target location'),
        'push': (task_instruction_2, 'move robot\'s gripper until the robot\'s gripper is above the target location'),
        'reach': (task_instruction_1, 'move robot\'s gripper until the robot\'s gripper is near the reach target'),
        'reach-wall': (task_instruction_1, 'move robot\'s gripper until the robot\'s gripper is above the reach target')
    }
    return instructions[task]

def robot_precond_list(cond_type, precond_name_list):
    if cond_type=='positive':
        cond_list = precond_name_list
    elif cond_type=='negative':
        cond_list = ['not '+x for x in precond_name_list]
    else:
        cond_list = []
    return cond_list

def robot_effect_list(cond_type, effect_name_list):
    if cond_type=='positive':
        effect_list = effect_name