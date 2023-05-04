

### 1 - Steps:

We have some code for the steps for this task.
Put them in the right order in the program.
"""

from robot_skills import robot_program

steps = [
    'Move the gripper in line with the hole from the side',
    'Line up the gripper with the top of the peg',
    'Move the peg to the hole until the gripper is over the hole',
    'Move gripper around the peg']

steps.sort()
for step in steps:
    print('##', step)
    robot_program.append_step(step)

"""## Steps:

Steps:

  1. Move gripper around the peg
  2. Line up the gripper with the top of the peg
  3. Move the gripper in line with the hole from the side
  4. Move the peg to the hole until the gripper is over the hole

### 2 - Code:

Now that we have the steps, we can write code to accomplish each step.

For `"Move gripper around the peg"`,

```
if check("the robot's gripper is not around the peg and the robot's gripper is open"):
    robot.drop("gripper around the peg")
```

For `"Line up the gripper with the top of the peg"`,

```
if check("the robot's gripper is not vertically aligned with the top of the peg"):
    robot.put("the gripper above the top of the peg")
```

For `"Move the gripper in line with the hole from the side"`,

```
if check("the robot's gripper is in front of the hole"):
    robot.push("gripper to left side of hole")
if check("the robot's gripper is not vertically aligned with the hole from the side"):
    robot.place("gripper above hole from the side")
```

For `"Move the peg to the hole until the gripper is over the hole"`,

```
if check("the robot's gripper is not above the hole"):
    robot.slide("the peg until the gripper is above the hole")
```
"""

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Move gripper around the peg
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
       