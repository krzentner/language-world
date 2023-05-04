
"""


#################################
############## Task #############
#################################


def create_task(task_dir, name):
    """Create a task from task directory."""

    if name == "reach":
        return task_reach.create_task(task_dir, name)

    if name == "button-press-topdown":
        return task_button_press_topdown.create_task(task_dir, name)

    if name == "peg-insert-side":
        return task_peg_insert_side.create_task(task_dir, name)

    if name == "drawer-close":
        return task_drawer_close.create_task(task_dir, name)

    if name == "drawer-open":
        return task_drawer_open.create_task(task_dir, name)

    if name == "door-open":
        return task_door_open.create_task(task_dir, name)

    if name == "pick-place":
        return task_pick_place.create_task(task_dir, name)

    if name == "push":
        return task_push.create_task(task_dir, name)

    if name == "window-close":
        return task_window_close.create_task(task_dir, name)

    if name == "window-open":
        return task_window_open.create_task(task_dir, name)


def create_task_from_name(task_dir, name):
    """Create a task from task directory."""

    if name == "reach":
        return task_reach.create_task(task_dir, name)

    if name == "button-press-topdown":
        return task_button_press_topdown.create_task(task_dir, name)

    if name == "peg-insert-side":
        return task_peg_insert_side.create_task(task_dir, name)

    if name == "drawer-close":
        return task_drawer_close.create_task(task_dir, name)

    if name == "drawer-open":
        return task_drawer_open.create_task(task_dir, name)

    if name == "door-open":
        return task_door_open.create_task(task_dir, name)

    if name ==