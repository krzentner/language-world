
"""


def get_task_desc(task, steps_only=False):
    task_name = task

    if steps_only:
        return steps_only_template.format(
            task_name,
            *_get_steps_only_description(task_name).split('\n')
        )
    return task_desc_template.format(
        task_name,
        *_get_task_description(task_name).split('\n')
    )


def get_step_desc(task, steps_only=False):
    if steps_only:
        return steps_only_step_template.format(
            *_get_steps_only_description(task).split('\n')
        )
    return step_desc_template.format(
        *_get_task_description(task).split('\n')
    )


def _get_task_description(task_name):
    task_desc = {
        'button-press-topdown': get_button_press_topdown_task_desc(),
        'door-open': get_door_open_task_desc(),
        'drawer-close': get_drawer_close_task_desc(),
        'drawer-open': get_drawer_open_task_desc(),
        'peg-insert-side': get_peg_insert_side_task_desc(),
        'reach': get_reach_task_desc(),
        'pick-place': get_pick_place_task_desc(),
        'plate-slide': get_plate_slide_task_desc(),
        'push': get_push_task_desc(),
        'window-close': get_window_close_task_desc(),
        'window-open': get_window_open_task_desc(),
    }[task_name]
    return task_desc


def _get_steps_only_description(task_name):
    task_desc = {
        'button-press-topdown': get_button_press_topdown_task_steps(),
        'door-open': get_door_open_task_steps(),
        'drawer-close': get_drawer_close_task_steps(),
        'drawer-open': get_drawer_open_task_steps(),
        'peg-insert-side': get_peg_insert_side_task_steps(),
        'reach': get_reach_task_steps(),
        'pick-place': get_pick_place_