

Your code can only use the `check` and `robot.move_gripper` functions above.

You can run your code using the following main file:

```
# main.py
import robot

def main():
    coffee_button(robot)

if __name__ == '__main__':
    main()
```
""".strip()

# We'll use this text later for grading your task
EXPLAIN_COFFEE_BUTTON_ANSWER = """
# coffee-button: push the button on the coffee machine
# Steps:
#  1. Line up the gripper as viewed from above
#  2. Push down on the button from the top

# Because this is "topdown", we just need to line up the gripper from above.
def coffee_button(robot):
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.move_gripper("vertically aligned with the coffee button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.move_gripper("near the coffee button")
```
""".strip()


class CoffeeButton(robot_text_answer.TextAnswerChecker):
    def __init__(self):
        super().__init__()

    def check_answers(self, answer_dict):
        code = answer_dict.get("coffee_button", "")
        if not code:
            return []
        if not code.strip():
            return [
                [
                    "Please write the code to perform the task: `coffee_button`.",
                    'Remember, the function should start with: ',
                    '```python\n# coffee-button: push the button on the coffee machine\ndef coffee_button(robot):',
                    '```',
                ],
            ]
        # We'll check if the code is correct using some test cases
        # TODO
        return []
[eod] [code]from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class ImgTag:
    name: str
    src: str


@dataclass_json
@dataclass
class TextTag:
    pass


@dataclass_json
@dataclass
class Tag:
    