

The code will control this robot:

```
robot.put(location): Move the robot's gripper to the specified location.
robot.grab(object): Grab the specified object with the gripper.
robot.place(location): Place the object being held to the specified location.
```

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Move gripper near cube
    #  2. Grab the cube
    #  3. Move the cube to the target location
    # First, we should put the gripper near the cube.
    if check("the robot's gripper is not near the cube"):
        robot.put("gripper near cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    # We closed the gripper, and the cube is still near the gripper, so maybe we grabbed it.
    # Try to move the cube to the target location.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.place("the cube in target location")
```

To make it simpler to write code, we defined some variables to hold common terms:

```
cube = "cube"
table = "table"
goal = "goal"
```

Please rewrite the code using these variables instead of repeating long phrases.
You can also define your own variables, if you would like:

```
# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Move gripper near cube
    #  2. Grab the cube
    #  3. Move the cube to the target location
    # First, we should put the gripper near the cube.
    if check("the robot's gripper is not near the cube"):
        robot.put("gripper near cube")
    # If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near