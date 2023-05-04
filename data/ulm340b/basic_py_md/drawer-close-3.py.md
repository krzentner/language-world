

Write the function.

If you'd like to see how well your program works, you can add the following:

```
def test():
    """Test robot on tasks."""
    if len(robot.sensor_labels()) > 0:
        robot.say("Sensors:")
        for sensor in robot.sensor_labels():
            robot.say("  " + sensor)
        robot.say("")

    while True:
        robot.say("Enter task:")
        task = input("> ")

        if task == "quit":
            break
        elif task == "help":
            robot.say("""Type in the name of a task, such as "push".
Type "help" to see the full list of tasks.
Type "quit" to end the program.""")
        elif task == "list":
            robot.say("""Available tasks:
door-open
drawer-open
peg-insert-side
push
reach
window-close
window-open""")
        else:
            task = getattr(robot, task)
            for i in range(10):
                task()
                robot.say("=")
    robot.say("Bye.")
```

And then call:

```
test()
```


import robot


def drawer_close(robot):
    """
    push the drawer close
    """
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.push("close the drawer")


def test():
    """Test robot on tasks."""
    if len(robot.sensor_labels()) > 0:
        robot.say("Sensors:")
        for sensor in robot.sensor_labels():
            robot.say("  " + sensor)
        robot.say("")

    while True:
        robot.say("Enter task:")
        task = input("> ")

        if task == "quit":
            break
        elif task == "help":
            robot.say("""Type in the name of a task, such as "push".
Type "help" to see the full list of tasks.
Type "quit" to end the program.""")