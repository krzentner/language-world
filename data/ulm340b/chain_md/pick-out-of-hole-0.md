
    Step 1: 
    Step 2: 
    Step 3: 
    Step 4: 
"""


def get_example_task(task):
    """Return the task instructions for the provided task."""
    if task == 'button-press-topdown':
        return example_task_button_press_topdown
    elif task == 'door-open':
        return example_task_door_open
    elif task == 'drawer-open':
        return example_task_drawer_open
    elif task == 'drawer-close':
        return example_task_drawer_close
    elif task == 'window-close':
        return example_task_window_close
    elif task == 'window-open':
        return example_task_window_open
    elif task == 'peg-insert-side':
        return example_task_peg_insert_side
    elif task == 'reach':
        return example_task_reach
    elif task == 'push':
        return example_task_push
    elif task == 'pick-place':
        return example_task_pick_place
    elif task == 'pick-out-of-hole':
        return example_task_pick_out_of_hole
    else:
        raise ValueError('No example found for task {}.'.format(task))


def get_example_actions(task):
    """Return the actions taken during the provided task."""
    if task == 'button-press-topdown':
        return example_actions_button_press_topdown
    elif task == 'door-open':
        return example_actions_door_open
    elif task == 'drawer-open':
        return example_actions_drawer_open
    elif task == 'drawer-close':
        return example_actions_drawer_close
    elif task == 'window-close':
        return example_actions_window_close
    elif task == 'window-open':
        return example_actions_window_open
    elif task == 'peg-insert-side':
        return example_actions_peg_insert_side
    elif task == 'reach':
        return example_actions_reach
    elif task == 'push':
        return example_actions_push
    elif task == 'pick-place':
        return example_actions_pick_place
    elif task == 'pick-out-of-hole':
        return example