

You may only use the following functions, and you may only use them once each:

```
robot.move()
robot.grab()
robot.turn()
robot.close()
robot.open()
robot.push()
robot.pull()
robot.reach()
robot.put()
robot.slide()
robot.align()
robot.drop()
robot.place()
robot.insert()
```

Please put your code in a file named `dial_turn.txt`. Once you're done, send it to us through the task interface. We have included an example solution in the file `dial_turn_example.txt`.
"""

# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not near dial"):
        robot.grab("dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not open"):
        robot.open("gripper around dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is open"):
        robot.turn("clockwise")


# dial-turn-v2: turn the dial from the other side
def dial_turn_v2(robot):
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not near dial"):
        robot.grab("dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not open"):
        robot.open("gripper around dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is open"):
        robot.turn("counterclockwise")


# dial-turn-v3: turn the dial and grab it from the top
def dial_turn_v3(robot):
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is not near dial"):
        robot.grab("dial")
    if