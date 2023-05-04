

Then enter a series of lines in this form:

```
if check("some description"):
    robot.action("description of action")
```

`check` returns a boolean describing whether its argument is true. The action is only performed if the condition is true.

> Your program should have 3 `if` statements.

Here are some useful checks:

```
# the robot's gripper is above the button
if check("the robot's gripper is above the button"):

# the robot's gripper is below the button
if check("the robot's gripper is below the button"):

# the robot's gripper is vertically aligned with the button
if check("the robot's gripper is vertically aligned with the button"):

# the robot's gripper is horizontally aligned with the button
if check("the robot's gripper is horizontally aligned with the button"):

# the robot's gripper is near the button
if check("the robot's gripper is near the button"):

# the robot's gripper is around the button
if check("the robot's gripper is around the button"):

# the button is above the robot's gripper
if check("the button is above the robot's gripper"):

# the button is below the robot's gripper
if check("the button is below the robot's gripper"):

# the button is vertically aligned with the robot's gripper
if check("the button is vertically aligned with the robot's gripper"):

# the button is horizontally aligned with the robot's gripper
if check("the button is horizontally aligned with the robot's gripper"):

# the button is near the robot's gripper
if check("the button is near the robot's gripper"):

# the button is inside the robot's gripper
if check("the button is inside the robot's gripper"):
```

Here are some useful actions:

```
# move the robot's gripper above the button
robot.put("gripper above button")

# move the robot's gripper below the button
robot.put("gripper below button")

# slide the robot's gripper above the button
robot.move("gripper above button")

# slide the robot's gripper below the button
robot.move("gripper below button")

# slide the robot's gripper to vertically align with the button
robot.align("gripper to button vertically")

# slide the robot's gripper to horizontally align with the button
robot