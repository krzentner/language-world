

You can write the rest of the code after that, but remember that it should do the task
`drawer-close`, which is to push the drawer close.
''',
  'task_name': 'drawer-close',
  'answer_type': 'language',
  'hints': [
    'There are a few ways you can approach this task.',
    'I would suggest starting by using the `reach` task as a starting point, as the '
    '`door-close` task has only one object.',
  ]
}

class RobotState(namedtuple('RobotState', ['step', 'objects', 'actions'])):
  def __repr__(self):
    return 'RobotState(step={}, objects={}, actions={})'.format(
      self.step,
      self.objects,
      self.actions,
    )

class Robot(object):
  def __init__(self, dsl, step, objects, actions):
    self.dsl = dsl
    self.step = step
    self.objects = objects
    self.actions = actions

  @property
  def object_list(self):
    return self.dsl.object_list

  def perform_task(self):
    step = 0
    objects = self.object_list
    actions = [True for _ in range(len(self.dsl.object_list))]
    while not self.task_done:
      if not self.dsl.actions[step][self.objects]:
        step += 1
        if step >= len(self.dsl.actions):
          break
      else:
        action, objects, actions = self.dsl.actions[step][self.objects]
        if action in ['put', 'move']:
          self.move_object(action, action, objects, actions, objects, actions)
        if action in ['drop', 'align', 'insert', 'slide', 'push', 'pull', 'close']:
          self.move_object(action, 'drop', objects, actions, objects, actions)
        if action in ['reach']:
          self.move_object(action, 'reach', objects, actions, objects, actions)
        if action in ['grab']:
          self.move_object(action, 'align', objects, actions, objects, actions)

  def move_object(self, action, type, objects, actions