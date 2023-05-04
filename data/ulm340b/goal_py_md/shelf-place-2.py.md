

## Input: A dictionary mapping names to objects

You are given a dictionary mapping variable names to objects:

```
objects = {
    'robot': None,
    'drawer handle': None,
    'drawer': None,
    'door handle': None,
    'door': None,
    'peg': None,
    'peg board': None,
    'button': None,
    'window handle': None,
    'window': None,
    'puck': None,
    'reach target': None,
    'target location': None,
}
```

The `robot` is the robot. The other objects are shown in the image.

You don't need to modify this dictionary.

## Input: A dictionary mapping names to relations

You are also given a dictionary mapping variable names to relations:

```
relations = {
    'the robot': None,
    'the robot's gripper': None,
    'robot.move_gripper()': None,
    'the robot\'s gripper': None,
    'the robot\'s gripper': None,
}
```

You don't need to modify this dictionary either.

For example, `robot.move_gripper("near the drawer handle")` is a relation
that takes one or more steps.
`drawer.is_open()` is a relation that takes no steps.

The relations you should have in your program will be shown below.

## Output: A function for moving the robot to perform a task

Your program should define the function `shelf_place(robot)`, which
controls the robot to achieve the goal of `shelf-place`.

## Output: A dictionary mapping tasks to relations

You should also create a dictionary mapping task names to a list of the relations that your program uses.

```
tasks = {
    'shelf-place': [],
    'other': [],
}
```

The list of relations should be the ones that are used in your program, in the order in which they appear in your program.
For example,

```
tasks = {
    'button-press-topdown': [
        'robot.move_gripper("above the button")',
        'robot.move_gripper("below the button")',
    ],
    'other': [],
}
```

When you submit your work, your answers will be evaluated and visualized.

To begin your work, click the blue **Open Code Editor** button.
[eod] [code]#!/usr/bin/env python3