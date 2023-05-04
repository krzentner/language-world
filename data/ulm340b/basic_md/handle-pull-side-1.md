'''


def get_task_name_to_instructions():
    instructions = OrderedDict()
    for task in tasks.values():
        instructions[task["task-name"]] = "\n".join(str(i) for i in task["task-steps"])
    return instructions


task_name_to_instructions = get_task_name_to_instructions()


class _ProseTaskDescription:
    def __init__(self, task, template_strings=None, **kw):
        if template_strings is None:
            template_strings = {}
        self._task = task
        self._task_name = task["task-name"]
        self._instructions = "\n".join(str(i) for i in task["task-steps"])
        self._instructions = template_strings.get(self._task_name, self._instructions)
        self._task_name = template_strings.get(self._task_name, self._task_name)
        self._params = kw

    def __str__(self):
        lines = []
        lines.append(self._task_name)
        lines.append(self._instructions)
        params_str = "Parameters:\n{}".format(" " * 4 + "\n".join("{}: {}".format(name, value)
                                                                  for name, value in self._params.items()))
        return "\n".join(lines) + params_str


def get_prose_task_description(template_strings):
    def f(task):
        name = task["task-name"]
        # hacky way to get the task description for each task.
        t = task_name_to_instructions[name]
        task["task-description"] = _ProseTaskDescription(task, template_strings)

    with ThreadPoolExecutor(max_workers=cpu_count()) as t:
        t.map(f, [t for t in tasks.values()])


class _TaskDescription:
    def __init__(self, task):
        self._task = task
        self._params = task["parameters"]

    @property
    def task_name(self):
        return self._task["task-name"]

    @property
    def task_description(self):
        return self._task["task-description"]

    @property
    def task_description_str(self):
        return str(self._task