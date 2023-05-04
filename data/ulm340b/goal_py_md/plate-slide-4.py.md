

As shown above, the function should take a single argument `robot`.

To check the status of the robot or move its gripper, you can use the functions:

- `check`: checks a status, return `True` or `False`
- `robot.move_gripper`: moves the robot's gripper

Here's an example. This code moves the gripper to be above the puck:

```
if check("the robot's gripper is not above puck"):
    robot.move_gripper("above the puck")
```

For each of the following, write the code to move the robot's gripper appropriately, using the text from the comment above to help you.

### Plate is not near the robot

If the robot's gripper is not near the plate, move the gripper to be near the plate.

'''), 15, 3,
        (
            'robot.move_gripper("below the plate")',
            'if check("the robot\'s gripper is not near plate"):',
            'robot.move_gripper("vertically aligned with the plate")',
        ),
        (
            'if check("the robot\'s gripper is not below the plate"):',
            'if check("the robot\'s gripper is not near plate"):',
            'robot.move_gripper("near the plate", close_gripper=True)',
        ),
        (
            'if check("the robot\'s gripper is above the plate and the robot\'s gripper is closed"):',
            'if check("the robot\'s gripper is near plate"):',
            'robot.move_gripper("near the plate")',
        ),
    ),

    (
    '''
### Plate is not horizontally aligned with the target

If the plate is not horizontally aligned with the target, slide it to be aligned with the target.
''', 15, 3,
        (
            'robot.move_gripper("around the plate")',
            'if check("plate is not vertically aligned with reach target"):',
            'robot.move_gripper("above the plate")',
        ),
        (
            'if check("the plate is not horizontally aligned with reach target"):',
            'if check("the plate is near the robot\'s gripper and the robot\'s gripper is not around the plate"):',
            'robot.move_gripper("near the plate", close_gripper=True)',
        ),
