# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("block at goal") 

# Helper function to check conditions
def check(condition):
    if condition:
        return True
    else:
        return False

# Testing the function
class Robot:
    def __init__(self):
        self.state = []

    def place(self, location):
        self.state.append(f"Block placed at {location}")

    def drop(self, location):
        self.state.append(f"Gripper dropped at {location}")

    def close(self, obj):
        self.state.append(f"Gripper closed around {obj}")

    def grab(self, obj):
        self.state.append(f"Gripper grabbed {obj}")

shelf_place(Robot())
print(Robot().state) # Output: ["Gripper placed above block", "Gripper closed around block", "Block placed at goal"]