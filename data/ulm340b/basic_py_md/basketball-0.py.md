

Then continue with lines of the form:

```
if check("condition"):
    robot.put("description")
```

where the code will only execute if the condition is met.

For reference, here's a vocabulary of commands the robot can understand.

```
# the robot can grab the object
robot.grab("object name")

# the robot can drop the object
robot.drop("object name")

# the robot can close the gripper
robot.close("object name")

# the robot can open the gripper
robot.open("object name")

# the robot can move the object
robot.move("object name")

# the robot can insert the object
robot.insert("object name")

# the robot can slide the object
robot.slide("object name")

# the robot can align the object
robot.align("object name")

# the robot can pull the object
robot.pull("object name")

# the robot can push the object
robot.push("object name")

# the robot can reach the target
robot.reach("target name")

# the robot can put the object at a place
robot.place("object name")

# the robot can put the object above another object
robot.put("object name", "on top of object")

# the robot can put the object above a target
robot.put("object name", "above target")

# the robot can put the object around an object
robot.put("object name", "around object")

# the robot can put the object near an object
robot.put("object name", "near object")

# the robot can put the object into an object
robot.put("object name", "into object")

# the robot can put the object over an object
robot.put("object name", "over object")
```

If you need more information about how to use the robot, the documentation can be accessed with
`help()`
''',
    # TODO (T67680386)
    'help': '''
```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's grip