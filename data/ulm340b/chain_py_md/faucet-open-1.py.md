

Please enter your instructions to the robot as a series of sentences, one per line.
You may use the following statements:


- `robot.grab()`: open the gripper and pick up an object
- `robot.place()`: put the held object down
- `robot.put()`: move the gripper
- `robot.reach()`: reach with the gripper
- `robot.pull()`: pull with the gripper
- `robot.push()`: push with the gripper
- `robot.insert()`: insert an object into another one
- `robot.align()`: line an object up with another one
- `robot.turn()`: turn an object around
- `robot.toggle()`: switch an object's state
- `robot.switch()`: switch an object's state by operating it
- `robot.slide()`: slide an object across another one


"""

# Please write a program to perform the last task, `faucet-open`.
def faucet_open(robot):
    # Steps:
    #  1. Put gripper on the faucet
    #  2. Turn the faucet left
    # First, put the gripper on the faucet.
    if check("the robot's gripper is not on the faucet"):
        robot.grab("faucet")
    # The robot's gripper is on the faucet. Turn the faucet.
    if check("the robot's gripper is on the faucet"):
        robot.turn("faucet left")

print("faucet-open-test")

# Please enter your instructions to the robot as a series of sentences, one per line.
def faucet_open_test(robot):
    if check("the robot's gripper is not on the faucet"):
        robot.grab("faucet")
    if check("the robot's gripper is on the faucet"):
        robot.turn("faucet left")
    if check("the robot's gripper is not on the faucet"):
        robot.grab("faucet")
    if check("the robot's gripper is on the faucet"):
        robot.turn("faucet left")
    if check("the robot's gripper is not on the faucet"):
        robot.grab("faucet")
    if check("the robot's gripper is on the faucet"):
        robot.turn("faucet left")
    if check("the robot's gripper is not on the faucet"):
        robot.grab("faucet")