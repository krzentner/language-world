
"""

# button-press-topdown
task = Task(id='button-press-topdown', name='button-press-topdown')
states = [
    # gripper not aligned with button
    {
        'type': State,
        'state_id': 's1',
        'task_id': task.id,
        'name': 'gripper not aligned with button',
        'state_start_conditions': {
            #'gripper_near_object': False,
            #'gripper_vertically_aligned_with_object': False
            'button_exists': True
        },
        'state_end_conditions': None,
        'actions_to_preform': [{
            'action': 'put gripper above button',
            'action_name': 'put gripper above button'
        }]
    },
    # gripper aligned with button
    {
        'type': State,
        'state_id': 's2',
        'task_id': task.id,
        'name': 'gripper aligned with button',
        'state_start_conditions': {
            #'gripper_near_object': False,
            'gripper_vertically_aligned_with_object': True
        },
        'state_end_conditions': None,
        'actions_to_preform': [{
            'action': 'push down on button',
            'action_name': 'push down on button'
        }]
    }
]

task.task_data.append(states[0])
task.task_data.append(states[1])

task.goal_states = ['s2']
task.initial_states = ['s1']

tasks.append(task)

# drawer-open
task = Task(id='drawer-open', name='drawer-open')
states = [
    # gripper not aligned with drawer handle
    {
        'type': State,
        'state_id': 's1',
        'task_id': task.id,
        'name': 'gripper not aligned with drawer handle',
        'state_start_conditions': {
            #'gripper_near_object': False,
            #'gripper_vertically_aligned_with_object': False
            'drawer_handle_exists