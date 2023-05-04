


## Test Case 1 ##
```python
def peg_unplug_side(robot):
    if check("the peg is not vertically aligned with the robot's gripper"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper"):
        robot.grab("peg")
    if check("peg is horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("the peg is not vertically aligned with the robot's gripper"):
        robot.pull("the peg up")
```


## Test Case 2 ##
```python
def peg_unplug_side(robot):
    if check("the peg is vertically aligned with the robot's gripper and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("peg is horizontally aligned with hole and the peg is not above hole"):
        robot.pull("peg to hole")
    if check("the peg is above hole and peg is not horizontally aligned with hole"):
        robot.align("peg with hole")
```


## Test Case 3 ##
```python
def peg_unplug_side(robot):
    if check("the peg is vertically aligned with the robot's gripper and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the peg is vertically aligned with the robot's gripper and the robot's gripper is not above peg"):
        robot.pull("the peg up")
```


## Test Case 4 ##
```python
def peg_unplug_side(robot):
    if check("the peg is vertically aligned with the robot's gripper and the robot's gripper is not around peg"):
        robot.put("gripper around peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the peg is vertically aligned with the robot's gripper"):
        robot.push