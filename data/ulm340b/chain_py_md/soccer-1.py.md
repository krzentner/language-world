

Then write code below it.

Good luck!
"""


def get_gripper_positions(text, m):
    lines = text.strip().split('\n')
    i = 0
    while i < len(lines) and lines[i].strip() != '    # Steps:':
        i += 1
    i += 1
    actions = []
    if lines[i].strip() == '    pass':
        actions.append('pass')
        i += 1
    i += 1
    while i < len(lines) and lines[i].strip() != '    pass' and lines[i].strip() != '    # Steps:':
        line = lines[i].strip().split(' ')
        actions.append([str(m.get_id(word)) if m.is_word(word) else word for word in line])
        i += 1
    return actions


def get_instruction_lines(text, m):
    lines = text.strip().split('\n')
    i = 0
    while i < len(lines) and lines[i].strip() != '    # Steps:':
        i += 1
    i += 1
    actions = []
    if lines[i].strip() == '    pass':
        i += 1
    i += 1
    while i < len(lines) and lines[i].strip() != '    pass' and lines[i].strip() != '    # Steps:':
        line = lines[i].strip().split(' ')
        if line[0] == 'robot':
            continue
        line_string = ' '.join(
            [str(m.get_id(word)) if m.is_word(word) else word for word in line[2:]])
        line_string = line_string.replace('"','')
        line_string = '"{}"'.format(line_string)
        actions.append(line_string)
        i += 1
    return actions


def get_state_to_action_map(m, actions, id_to_actions):
    m.set_state([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3