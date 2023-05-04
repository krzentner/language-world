


"""


def get_task_specific_instructions(task_name):
    if task_name == 'button-press-topdown':
        return TASK_BUTTON_PRESS
    elif task_name == 'door-open':
        return TASK_DOOR_OPEN
    elif task_name == 'drawer-open':
        return TASK_DRAWER_OPEN
    elif task_name == 'drawer-close':
        return TASK_DRAWER_CLOSE
    elif task_name == 'window-close':
        return TASK_WINDOW_CLOSE
    elif task_name == 'window-open':
        return TASK_WINDOW_OPEN
    elif task_name == 'peg-insert-side':
        return TASK_PEG_INSERT
    elif task_name == 'reach':
        return TASK_REACH
    elif task_name == 'push':
        return TASK_PUSH
    elif task_name == 'pick-place':
        return TASK_PICK_PLACE
    elif task_name == 'pick-out-of-hole':
        return TASK_PICK_OUT_OF_HOLE
    elif task_name == 'unplug-usb':
        return TASK_UNPLUG_USB
    else:
        raise Exception("Task not recognized.")


def create_task_specific_instructions_dataset():
    task_to_instructions = {}

    task_to_instructions['button-press-topdown'] = TASK_BUTTON_PRESS
    task_to_instructions['door-open'] = TASK_DOOR_OPEN
    task_to_instructions['drawer-open'] = TASK_DRAWER_OPEN
    task_to_instructions['drawer-close'] = TASK_DRAWER_CLOSE
    task_to_instructions['window-close'] = TASK_WINDOW_CLOSE
    task_to_instructions['window-open'] = TASK_WINDOW_OPEN
    task_to_instructions['peg-insert-side'] = TASK_PEG_INSERT
    task_to_instructions['reach'] = TASK_REACH
    task_to_instructions['push'] = TASK_PUSH
    task_to_instructions['pick-place'] = TASK_PICK_PLACE
    task_to_instructions['pick-out-of-hole'] = TASK_PICK_OUT_OF_HOLE
    task_to_instructions['unplug-usb'] = TASK_UNPLUG_USB

    data = {}
    data['task_