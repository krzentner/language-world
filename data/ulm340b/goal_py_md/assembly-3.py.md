
''')


def get_object_locations_and_attributes(task_name):
    task = get_data_files(task_name)
    task_data = task.get_data()

    obj_locs = task_data['object_locations']
    obj_attrs = task_data['object_attributes']
    return obj_locs, obj_attrs


def get_task_description(task_name, task_idx):
    """Get a description of the task with <task_idx> in <task_name>'s description."""
    if task_name == 'pick-place':
        obj_names = ['puck', 'target_location']
        objs = obj_names[task_idx]
        return 'put the puck in the target location'
    elif task_name == 'push':
        obj_names = ['puck', 'target_location']
        objs = obj_names[task_idx]
        return 'slide the puck to the target location'
    elif task_name == 'button-press-topdown':
        obj_names = ['button']
        objs = obj_names[task_idx]
        return 'push the button down from above'
    elif task_name == 'reach':
        obj_names = ['reach_target']
        objs = obj_names[task_idx]
        return 'reach to the target location'
    elif task_name == 'door-open':
        obj_names = ['door_handle']
        objs = obj_names[task_idx]
        return 'pull the door open'
    elif task_name == 'drawer-close':
        obj_names = ['drawer_handle']
        objs = obj_names[task_idx]
        return 'push the drawer closed'
    elif task_name == 'drawer-open':
        obj_names = ['drawer_handle']
        objs = obj_names[task_idx]
        return 'pull the drawer open'
    elif task_name == 'window-close':
        obj_names = ['window_handle']
        objs = obj_names[task_idx]
        return 'slide the window closed to the right'
    elif task_name == 'window-open':
        obj_names = ['window_handle']
        objs = obj_names[task_idx]
        return 'slide the window open to the left'
    elif task_name == 'assembly'