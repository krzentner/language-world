

If you get stuck, you can ask for hints by saying "i'm stuck".
"""

# basketball: put the ball into into the hoop
def basketball(robot):

    # Steps:
    #  1. Put gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Line up the gripper with the hoop as seen from the front
    #  4. Raise the hoop up so the ball goes in
    # First, put the gripper above the ball.
    if check("the robot's gripper is not vertically aligned with the ball"):
        robot.move_gripper("vertically aligned with the ball")
    # If the ball becomes left of the gripper, go back to putting the gripper
    # above the ball.
    # Because the ball is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("the ball is not left of the robot's gripper and the ball is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the ball", close_gripper=True)
    # As long the gripper is still mostly around the ball and the ball isn't lined
    # up with the hoop, line up the ball with the hoop.
    if check("the ball is horizontally aligned with the hoop"):
        robot.move_gripper("above the ball")
    # If the ball is lined up with the hoop to the side, insert it.
    if check("the robot's gripper is forward aligned with the ball and the ball is not horizontally aligned with the hoop"):
        robot.move_gripper("horizontally aligned with the hoop")[eod] [code]from bs4 import BeautifulSoup

import nltk
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

def cleanText(input):
    try:
        if input == None:
            return ''
        else:
            input = input.lower()
            input = input.replace('\n','')
            input = input.replace('\t','')
            return input
    except:
        return ''


def createNgrams(text):
    text = cleanText(text)

    tokens = tokenizer.tokenize(text)
  