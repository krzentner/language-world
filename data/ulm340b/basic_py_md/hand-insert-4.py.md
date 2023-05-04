

Your program must be able to perform the task in both the scenes that follow.


"""



def hand_insert(robot):
    if check("the robot's gripper is not near the puck"):
        robot.place("gripper around puck")
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.grab("puck")
    if check("the robot's gripper is around puck"):
        robot.place("puck at goal")
    
[eod] [code]from .base import BaseComponent

from kivy.factory import Factory
from kivy.uix.button import Button


class ButtonComponent(BaseComponent):
    @property
    def kwargs(self):
        return {}

    def create_component(self):
        self.button = Factory.Button(**self.kwargs)
        return self.button

    def apply_binding(self, binding):
        self.button.bind(on_press=lambda b: binding.call(self.container))


class Button(BaseComponent):
    """
    Button Component
    """
    COMPONENT_NAME = 'Button'

    def __init__(self, text, color='', background_color='', size_hint=None, background_image=None, button_args=None,
                 **kwargs):
        super().__init__()
        self.component = ButtonComponent()
        self.kwargs = kwargs
        self.button_args = button_args

        self.component.kwargs['text'] = text
        self.component.kwargs['color'] = color
        self.component.kwargs['background_color'] = background_color
        self.component.kwargs['size_hint'] = size_hint
        self.component.kwargs['background_image'] = background_image
        self.component.kwargs.update(self.kwargs)

    def create_component(self):
        self.container = self.component.create_component()
        self.container.kwargs.update(self.button_args)

    def apply_binding(self, binding):
        self.component.apply_binding(binding)


[eod] [code]#
#

# Copyright