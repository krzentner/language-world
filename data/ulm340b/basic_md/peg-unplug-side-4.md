
'''


def _process_prompt_text(text):
    processed_lines = []
    for line in text.strip().split('\n'):
        if line and not line.isspace():
            processed_lines.append(line)
    return '\n'.join(processed_lines)


def _get_instructions(
        task_name,
        state_rep_type,
        policy_type,
):
    task_to_instructions = {
        "drawer-open": _get_drawer_open_instructions,
        "door-open": _get_door_open_instructions,
        "button-press-topdown": _get_button_press_instructions,
        "reach": _get_reach_instructions,
        "window-close": _get_window_close_instructions,
        "window-open": _get_window_open_instructions,
        "push": _get_push_instructions,
        "pick-place": _get_pick_place_instructions,
        "drawer-close": _get_drawer_close_instructions,
        "peg-insert-side": _get_peg_insert_side_instructions,
        "peg-unplug-side": _get_peg_unplug_side_instructions,
        "peg-insert-topdown": _get_peg_insert_topdown_instructions,
        "peg-unplug-topdown": _get_peg_unplug_topdown_instructions
    }
    if task_name not in task_to_instructions:
        raise ValueError(f"Unknown task name: {task_name}")
    return task_to_instructions[task_name](state_rep_type, policy_type)


def _get_drawer_open_instructions(state_rep_type, policy_type):
    instr_to_policy = {
        "put": "place",
        "grab": "grasp",
        "around": "open"
    }
    if state_rep_type != "image_state":
        raise ValueError("drawer_open only implemented for image_state")
    if policy_type not in instr_to_policy:
        raise ValueError("Drawer open task only implemented for {} policies".format(set(instr_to_policy.keys())))
    return [_process_prompt_text(INSTRUCTIONS_TEMPLATE_DRAWER_OPEN)]


def _get_door_open_instructions(state_rep_type, policy_type):
    instr_to_