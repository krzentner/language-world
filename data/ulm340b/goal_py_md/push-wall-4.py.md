

And make a program to achieve the goal from the `robot`.
Use `check(statement, close_gripper=False)` to determine whether the given `statement` is true, and to close the gripper.
Use `robot.move_gripper("above the table", close_gripper=True)` to move the gripper to the given location, and to close the gripper.
To write the program, use this function.

```
def check(statement, close_gripper=False):
    # Use these functions.
    def check(statement, close_gripper=False):
        '''Return the given `statement` if the gripper is closed and `statement`
        is true. Otherwise, return the empty string.
        '''
        if check("the robot's gripper is closed"):
            if check(statement):
                return statement
        return ""

    def move_gripper(destination, close_gripper=False):
        '''Move the robot's gripper to `destination`, closing the gripper if
        `close_gripper` is true.
        '''
        move_gripper(destination, close_gripper=close_gripper)

    return statement
```

Here are some example statements that can be put in `check`.
The gripper is closed when these statements are true.
You may want to use them in your program.

```
the robot's gripper is above object
the robot's gripper is left of object
the robot's gripper is right of object
the robot's gripper is above the target location
the robot's gripper is left of the target location
the robot's gripper is right of the target location
the robot's gripper is around object
the robot's gripper is vertically aligned with object
the robot's gripper is in front of object
the robot's gripper is horizontally aligned with object
the robot's gripper is near object
the robot's gripper is left of the table
the robot's gripper is above the table
the robot's gripper is near the table
the robot's gripper is closed
```

Here is the function to move the gripper.
You don't need to edit this part.

```
def move_gripper(destination, close_gripper=False):
    '''Move the robot's gripper to `destination`, closing the gripper if
    `close_gripper` is true.
    '''
    move_gripper(destination, close_gripper=close_gripper)
```

When you are done, call `push_wall(