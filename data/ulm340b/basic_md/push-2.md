"""


def get_task_instructions(task_id):
    """Return instructions for the specified task.

    Args:
        task_id (str): Task ID.

    Returns:
        A dict with the following keys:
            - instruction (str): The full instruction (usually a paragraph of text).
            - bullet_points (str[]): Short bullet point summary of instruction (usually just steps).
            - bullet_points_raw (str[]): Bullet points as they appear in the instruction.
            - task (dict): The task dictionary from `task_graph.py`.
    """
    try:
        return TASK_INSTRUCTIONS[task_id]
    except KeyError:
        return None


def get_tasks(task_ids=None):
    """Return all task IDs.

    Args:
        task_ids (str[]): Optional task IDs. Defaults to None.

    Returns:
        str[]: A list of all task IDs.
    """
    return list(TASK_INSTRUCTIONS.keys()) if task_ids is None else task_ids


# noinspection DuplicatedCode
def get_instructions(task_ids=None):
    """Return instructions for all tasks.

    Args:
        task_ids (str[]): Optional task IDs. Defaults to None.

    Returns:
        dict: A dictionary mapping task ID to its instruction.
    """
    task_ids = get_tasks(task_ids)
    instructions = {task_id: get_task_instructions(task_id) for task_id in task_ids}
    return instructions


# noinspection DuplicatedCode
def get_instruction(task_id, task_ids=None):
    """Return instruction for a task.

    Args:
        task_id (str): Task ID.
        task_ids (str[]): Optional task IDs. Defaults to None.

    Returns:
        The task's instruction if it exists, otherwise None.
    """
    task_ids = get_tasks(task_ids)
    instructions = get_instructions(task_ids)
    try:
        return instructions[task_id]
    except KeyError:
        return None


def get_all_tasks_and_instructions(task_ids=None):
    """Return all tasks and their instructions.

    Args:
        task_ids (str[]): Optional task IDs. Defaults to None.

    Returns:
        A list of dictionaries, each containing a task and its instruction.