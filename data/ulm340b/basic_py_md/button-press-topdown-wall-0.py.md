
'''

button_press_topdown_wall_def = """
# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
"""

def get_button_press_topdown_wall_program(student_code, testcase):
    return f"```\n{button_press_topdown_wall_def}```\n```\n{student_code}\n```"

def grade(student_code, target_code):
    student_code_lines = student_code.splitlines()
    target_code_lines = target_code.splitlines()

    correct = 0

    # check that student_code begins with the button_press_topdown_wall_def
    correct += int(student_code_lines[0] == button_press_topdown_wall_def)

    if correct < 1:
        return 0

    # check that student_code includes `if check("the robot's gripper is not above button"):``
    correct += int(
        "if check(" in student_code_lines[1]
        and "gripper is not above button" in student_code_lines[1]
    )

    if correct < 1:
        return 0

    # check that student_code includes `robot.put("gripper above button")`
    correct += int("put(" in student_code_lines[2] and "gripper above button") in student_code_lines[2])

    return correct
[eod] [code]import sys
import os

import pandas as pd
from pandas.plotting import scatter_matrix

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model import train_model
from preprocess import preprocess

def main():

    # read in all the csv files and save to dataframe
    # data = pd.read_csv("titanic_data.csv")
    df = pd.read_csv("/home/pablo/Documents/PycharmProjects/titanic/dataset/train.csv")
    df = preprocess(df)

    # inspect dataframe
    df.describe()
    scatter_matrix(df)

    # separate out the features and target variable from data frame
    X = df.drop("