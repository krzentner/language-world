

Then, write code for it in a way that follows the same style as all the other
code.
For example, if there's a step "If the gripper is not near the drawer handle,
move it to the drawer handle" then you could write the following code to
perform it:

```
# If the gripper is not near the drawer handle, move it to the drawer handle.
if check("the robot's gripper is not near the drawer handle"):
    robot.move("gripper to drawer handle")
```
"""

import re

with open(
        'drawer-open.txt', 'r', encoding='utf-8') as file:
    drawer_open = file.read()


def parse(text):
    def get_action(text):
        m = re.search('(.*): (\w*) (\w*) to (.*)', text)
        verb, preposition, phrase = m.groups()[1:4]
        if verb == 'put':
            return 'put'
        elif verb == 'push':
            return 'push'
        elif verb == 'drop':
            return 'drop'
        elif verb == 'pull':
            return 'pull'
        elif verb == 'grab':
            return 'grab'
        elif verb == 'slide':
            return 'slide'
        elif verb == 'align':
            return 'align'
        elif verb == 'move':
            return 'move'
        else:
            raise Exception(f"Unexpected verb '{verb}'")
    lines = [line for line in text.split('\n') if line]
    lines.pop(0)
    lines.pop(-1)
    result = []
    indents = 0
    for line in lines:
        indents += line.count(' ')
        if line.count(' ') < 4:
            start = line.find('"""')
            indents += start // 2
            indents -= start // 2
    indents /= len(lines)
    for line in lines:
        indents = line.count(' ')
        if line.count(' ') < 4:
            start = line.find('"""')
            indents += start // 2
            indents -= start // 2
        if indents == 0:
            result.append(line)
        elif indents == 2