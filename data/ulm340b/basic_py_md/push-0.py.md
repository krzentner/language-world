
"""

code_template = '''\
# TASKNAME: PERFORM TASK
# INPUT: A robot instance
def TASKNAME(robot):
    # code goes here
'''

code_template_w_check = '''\
# TASKNAME: PERFORM TASK
# INPUT: A robot instance
def TASKNAME(robot):
    if check("CONDITION"):
        # code goes here
'''

if TASK_NAME == 'button_press_topdown':
    task_name = 'button press topdown'
    code_template = code_template_w_check
    task_description = '''\
The robot's gripper is open and above the button, and the robot's gripper is not vertically aligned with the button'''

elif TASK_NAME == 'drawer_open':
    task_name = 'drawer open'
    code_template = code_template_w_check
    task_description = '''\
The robot's gripper is open and near the drawer handle, and the robot's gripper is not vertically aligned with the drawer handle'''

elif TASK_NAME == 'peg_insert_side':
    task_name = 'peg insert side'
    code_template = code_template_w_check
    task_description = '''\
The peg is above the hole, and the robot's gripper is open and not above the peg'''

elif TASK_NAME == 'door_open':
    task_name = 'door open'
    code_template = code_template_w_check
    task_description = '''\
The robot's gripper is open and above the door handle, and the robot's gripper is not vertically aligned with the door handle'''

elif TASK_NAME == 'drawer_close':
    task_name = 'drawer close'
    code_template = code_template_w_check
    task_description = '''\
The drawer is open, and the robot's gripper is open and above the drawer handle'''

elif TASK_NAME == 'window_close':
    task_name = 'window close'
    code_template = code_template_w_check
    task_description = '''\
The window is open, and the robot's gripper is open and above the window handle'''

elif TASK_NAME == 'window_open':
    task_name = 'window open'
    code_template = code_template_w_check
    task_description = '''\
The window is closed