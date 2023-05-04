

...and write the code for the function after it.

## Example ##

For example, let's write a program for a new task: to pull open a drawer from the top.
I'll call this task `drawer-pull`.

The robot should start from the same position as before:

```
+------+     +---+     +---------+     +------+     +---+
|      |     |    |     |         |     |      |     |    |
|      |     |    |     |         |     |      |     |    |
+------+     +---+     |         |     +------+     +---+
```

The robot should end with the drawer being opened to the side, like this:

```
+------+     +---+     +---------+
|      |     |    |     |         |
|      |     |    |     |         |
+------+     +---+     |         |
```

Here's how I would write it.

First, I'll write a function header.

```
def drawer_pull(robot):
```

Then, I'll write a comment describing how to break down the task into simple steps:

```
def drawer_pull(robot):
    # Steps:
    #  1. Drop the gripper around the drawer handle
    #  2. Pull open the drawer
```

Then, I'll implement the steps with `check` and `if`.

```
def drawer_pull(robot):
    # Steps:
    #  1. Drop the gripper around the drawer handle
    #  2. Pull open the drawer
    # As long as the robot's gripper is above the drawer handle and not around
    # it, we should drop it around the handle.
    if check("the robot's gripper is above drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    # As long as the gripper is around the drawer handle, we can just pull the
    # drawer open.
    if check("the robot's gripper is around drawer handle"):
        robot.pull("drawer open")
```

Then, we can make sure the function works:

```
if __name__ == '__main__':
    robot = Robot()
    robot.run('drawer-pull', [drawer_pull])
```

## Details ##

I won't be able to give you feedback on your answer, or tell