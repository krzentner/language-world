

And then provide the steps to execute this program.  The steps have the form of `check(description)` and `robot.action(description)`.

Thank you for your help.
"""


class Instruction:
    def __init__(self, name, check, action, description, params, arg, arg2):
        self.name = name
        self.check = check
        self.action = action
        self.description = description
        self.params = params
        self.arg = arg
        self.arg2 = arg2


instructions = {
    "drawer-close": Instruction("drawer-close", False, False, "drawer closed", [], 2, 3),
    "drawer-open": Instruction("drawer-open", False, False, "drawer open", [], 2, 3),
    "door-open": Instruction("door-open", False, False, "door open", [], 2, 3),
    "handle-pull": Instruction("handle-pull", False, False, "handle pulled up", [], 2, 3),
    "pick-place": Instruction("pick-place", False, False, "pick and place object", [], 2, 3),
    "push": Instruction("push", False, False, "push puck to goal", [], 2, 3),
    "button-press-topdown": Instruction(
        "button-press-topdown", False, False, "press button top down", [], 2, 3
    ),
    "window-close": Instruction("window-close", False, False, "close window", [], 2, 3),
    "window-open": Instruction("window-open", False, False, "open window", [], 2, 3),
    "peg-insert-side": Instruction(
        "peg-insert-side", False, False, "peg inserted from side", [], 2, 3
    ),
    "reach": Instruction("reach", False, False, "reach to goal", [], 2, 3),
}


def get_all_actions():
    actions = []
    for k in instructions.keys():
        instructions[k].action = True
        actions.append(k)

    if instructions["handle-pull"].name not in actions:
        actions.append(instructions["handle-pull"].name)
        instructions["handle-pull"].action = True

    if instructions["push"].name not in actions:
        actions.append(instructions["push"].name)
        instructions["push"].action = True

    return actions


actions = []

# print actions