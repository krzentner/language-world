

Then, fill in the rest of the body of the function to achieve `sweep-into`. 

You may also use: `if check("the robot's gripper is near the object"): robot.grab("object");` and `if check("the robot's gripper is not near object"): robot.drop("object");` 

"""

# Here's a little code to make testing simpler:
class Robot:
    def __init__(self):
        self.state = {"pos": "left", "open": False, "left_of": False}

    def check(self, state):
        return eval(f"self.state['{state}']")

    def get(self, state):
        return eval(f"self.state['{state}']")

    def put(self, state, value):
        eval(f"self.state['{state}'] = {value}")

    def reach(self, value):
        print(f"reaching to {value}")

    def move(self, value):
        print(f"move to {value}")

    def slide(self, value):
        print(f"slide {value}")

    def drop(self, value):
        print(f"dropping {value}")

    def grab(self, value):
        print(f"grabbing {value}")

    def pull(self, value):
        print(f"pulling {value}")

    def align(self, value):
        print(f"aligning {value}")

    def insert(self, value):
        print(f"inserting {value}")

    def open(self, value):
        print(f"opening {value}")

    def close(self, value):
        print(f"closing {value}")

    def push(self, value):
        print(f"pushing {value}")

    def place(self, value):
        print(f"placing {value}")

def button_press_topdown(robot):
    if robot.check("robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if robot.check("robot's gripper is vertically aligned with button"):
        robot.push("down on button")

def drawer_open(robot):
    if robot.check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if robot.check("robot's gripper is vertically aligned with drawer handle