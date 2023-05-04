

and make sure to call the appropriate `robot` methods (like `robot.push` and `robot.pull`) to perform the task.

When you're done, send the code back to me, and I'll ask you a few questions about it.
"""
    def answer_question(self) -> str:
        try:
            return_val = eval(self.user_input)
            if return_val is None:
                return_val = ""
            return return_val
        except SyntaxError as err:
            self.logger.error("Uncaught Syntax Error!  Please report this to the bot's creator.")
            self.logger.error(err)
            return ""
        except Exception as err:
            self.logger.error("Uncaught Exception!  Please report this to the bot's creator.")
            self.logger.error(err)
            return ""
    def next_question(self):
        return "13"

class Question13(Question):
    def __init__(self):
        super().__init__()
        self.question = """
        I have another task for you. It's called `plate-slide-front`.

In this task, the robot is standing in front of a plate. The robot has to slide the plate from its current position (away from the robot) to a target position on the right.

The robot's gripper is closed at the beginning of the task.

You will need to write the code for this function:

```
# plate-slide-front: slide the plate towards the target location
def plate_slide_front(robot):
```

and make sure to call the appropriate `robot` methods (like `robot.push` and `robot.pull`) to perform the task.

Please begin with the provided code below and add your code inside the function.
"""
    def answer_question(self) -> str:
        try:
            return_val = eval(self.user_input)
            if return_val is None:
                return_val = ""
            return return_val
        except SyntaxError as err:
            self.logger.error("Uncaught Syntax Error!  Please report this to the bot's creator.")
            self.logger.error(err)
            return ""
        except Exception as err:
            self.logger.error("Uncaught Exception!  Please report this to the bot's creator.")
            self.logger.error(err)
            return ""
    def next_question(self):
        return "14"

class Question14(Question):
    def __init