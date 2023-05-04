
''')

BOX_CLOSE = '''
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper above the lid
    #  2. Grab the lid with the gripper
    #  3. Move the lid towards the box
    # First, put the gripper above the lid.
    if check("the robot's gripper is not vertically aligned with lid"):
        robot.move_gripper("vertically aligned with lid")
    # If the gripper isn't around the lid, put it around the lid.
    if check("the robot's gripper is not around lid and the robot's gripper is open"):
        robot.move_gripper("near the lid", close_gripper=True)
    # As long the gripper is still mostly around the lid and the lid isn't above
    # the box, move the lid towards the box.
    if check("the robot's gripper is around lid"):
        robot.move_gripper("above lid")
'''

def check(description, robot):
    return True

def move_gripper(description, close_gripper=False):
    pass

def test_box_close():
    assert 'if check("the robot\'s gripper is not vertically aligned with lid"):' in box_close
    assert 'if check("the robot\'s gripper is not around lid and the robot\'s gripper is open"):' in box_close
    assert 'if check("the robot\'s gripper is around lid"):' in box_close
[eod] [code]# coding: utf-8
from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import auth
from . import user
from . import book
from . import admin_user
from . import admin_book
from . import category
[eod] [code]from flask import Flask, request, jsonify

app = Flask(__name__)


class Food:
    id: str
    name: str
    price: str
    detail: str

    def __init__(self, id, name, price, detail):
        self.id = id
        self.name = name
        self.price = price
        self.detail = detail


class FoodList