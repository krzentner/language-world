

"""


class InstructionTask(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_instruction(self, instruction_index):
        if self.name == "drawer-open":
            return InstructionTask.drawer_open_get_instruction(instruction_index)
        elif self.name == "button-press-topdown":
            return InstructionTask.button_press_topdown_get_instruction(instruction_index)
        elif self.name == "drawer-close":
            return InstructionTask.drawer_close_get_instruction(instruction_index)
        elif self.name == "door-open":
            return InstructionTask.door_open_get_instruction(instruction_index)
        elif self.name == "window-close":
            return InstructionTask.window_close_get_instruction(instruction_index)
        elif self.name == "window-open":
            return InstructionTask.window_open_get_instruction(instruction_index)
        elif self.name == "peg-insert-side":
            return InstructionTask.peg_insert_side_get_instruction(instruction_index)
        elif self.name == "reach":
            return InstructionTask.reach_get_instruction(instruction_index)
        elif self.name == "push":
            return InstructionTask.push_get_instruction(instruction_index)
        elif self.name == "pick-place":
            return InstructionTask.pick_place_get_instruction(instruction_index)
        elif self.name == "sweep":
            return InstructionTask.sweep_get_instruction(instruction_index)
        else:
            raise Exception("Invalid task name: {}".format(self.name))

    def get_instruction_index(self, instruction):
        if self.name == "drawer-open":
            return InstructionTask.drawer_open_get_instruction_index(instruction)
        elif self.name == "button-press-topdown":
            return InstructionTask.button_press_topdown_get_instruction_index(instruction)
        elif self.name == "drawer-close":
            return InstructionTask.drawer_close_get_instruction_index(instruction)
        elif self.name == "door-open":
            return InstructionTask.door_open_get_instruction_index(instruction)
        elif self.name == "window-close":
            return InstructionTask.window_close_get_instruction_index(instruction)
        elif self.name == "window-open":
            return InstructionTask.window_open