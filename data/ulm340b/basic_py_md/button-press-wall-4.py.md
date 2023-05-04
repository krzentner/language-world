
"""
from programy.parser.pattern.triplets.find_all_triplets import find_all_triplets
from programy.parser.pattern.triplets.extract_triplets_from_string import extract_triplets_from_string
from programy.parser.pattern.triplets.extract_triplets import extract_triplets

from programytest.parser.base import ParserTestsBaseClass


class MockControl(object):

    def __init__(self, *vars):
        self.vars = vars

    def __contains__(self, item):
        return item in self.vars

    def __getitem__(self, item):
        return self.vars.get(item)


class ParserTests(ParserTestsBaseClass):

    def test_extract_triplets(self):
        self.assertEqual(extract_triplets("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"),
                         ["the robot's gripper is not vertically aligned with the window handle",
                          "the robot's gripper is below the window handle"])

        self.assertEqual(extract_triplets("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"),
                         ["the robot's gripper is vertically aligned with drawer handle",
                          "the robot's gripper is not around drawer handle"])

        self.assertEqual(extract_triplets("the robot's gripper is around drawer handle"),
                         ["the robot's gripper is around drawer handle"])

        self.assertEqual(extract_triplets("the robot's gripper is not vertically aligned with drawer handle"),
                         ["the robot's gripper is not vertically aligned with drawer handle"])

    def test_find_all_triplets(self):

        task = 'button-press-wall: push the button from the front with a short wall in the way'
        self.assertEqual(find_all_triplets(task),
                         [['button-press-wall', 'button-press-wall: push the button from the front with a short wall in the way']])

        task = 'def button_press_wall(robot):'
        self.assertEqual(find_all_triplets(task),
                         [['button_press_wall', 'def button_press_wall(robot):']])

        self.assertEqual(find_all_triplets("if check('the robot'