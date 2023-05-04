

Your code should be as much like the examples as possible, but may differ as appropriate for the task.

Write your code within the following box (don't touch the rest of the file).
```

## Enter your code here.
```

def check(condition):
    return condition

def robot_move(instruction):
    with open(INSTRUCTION_FILE) as f:
        content = f.readlines()
    with open(INSTRUCTION_FILE, 'w') as f:
        for line in content:
            if 'INSTRUCTION' not in line:
                f.write(line)
            else:
                f.write(instruction + '\n')

robot_move(task_name + '\n\n' + ' ' * 4 +
           'the robot's gripper is below peg\n')
robot_move(' ' * 4 + 'the robot's gripper is not vertically aligned with peg\n\n')
robot_move(task_name + '\n\n')

INSTRUCTION_FILE = '/u/nlp/asmith/scratch/instructions.txt'

class Robot:
    def __init__(self, task_name, *args):
        self.task_name = task_name
        self.args = args
        self.commands = {
            'put': lambda x: robot_move('%s: put %s\n' % (self.task_name, x)),
            'grab': lambda x: robot_move('%s: grab %s\n' % (self.task_name, x)),
            'close': lambda x: robot_move('%s: close %s\n' % (self.task_name, x)),
            'move': lambda x: robot_move('%s: move %s\n' % (self.task_name, x)),
            'drop': lambda x: robot_move('%s: drop %s\n' % (self.task_name, x)),
            'pull': lambda x: robot_move('%s: pull %s\n' % (self.task_name, x)),
            'push': lambda x: robot_move('%s: push %s\n' % (self.task_name, x)),
            'align': lambda x: robot_move('%s: align %s\n' % (self.task_name, x)),
            'slide': lambda x: robot_move('%s: slide %s\n' % (self.task_name, x