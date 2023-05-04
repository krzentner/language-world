

### Step 1: Hello! ###

The robot responds to two types of commands.

The first type of command simply moves the gripper to a specific location, like `robot.place("gripper above puck")`.
These commands take one argument, a string that includes the desired location, such as `"gripper above puck"`.

```
if check("the robot's gripper is not above the puck"):
    robot.place("gripper above puck")
```

The second type of command moves something other than the robot's gripper.
These commands take two arguments, the object being moved and the desired location, like `robot.insert("peg into hole")`.
The first argument is a string that includes the object, such as `"peg"`, and the second argument is a string that includes the desired location, such as `"into hole"`.

```
if check("peg is horizontally aligned with hole"):
    robot.insert("peg into hole")
```

Here are all of the locations we will use today:

```
the goal
away from drawer
left of window handle
right of window handle
above drawer handle
above puck
above button
above peg
around door handle
above door handle
below door handle
almost vertically aligned with door handle
around drawer handle
vertically aligned with drawer handle
vertically aligned with the robot's gripper
vertically aligned with button
left of the robot's gripper
forward aligned with drawer handle
forward aligned with the robot's gripper
forward aligned with peg
near the window handle
near puck
near the robot's gripper
near reach target
horizontally aligned with hole
not above the puck
not left of the robot's gripper
not near the drawer handle
not near the window handle
not vertically aligned with drawer handle
not almost vertically aligned with door handle
not vertically aligned with peg
not near puck
not around drawer handle
not around door handle
```

And here are the objects we can move:

```
the gripper
drawer handle
the drawer
door handle
peg
```

Finally, the robot can grab the following objects:

```
the peg
door handle
drawer handle
```

### Step 2: Hello! ###

Before I let you control the robot, please describe for me the goal of `lever-pull`.

```
# lever-pull: rotate the lever up
def lever_pull(robot):
```

### Step 3: Hello! ###

When programming the robot, we can refer to the objects by name.
We can say `"lever"` instead of `"object-3"` and `"gripper"`