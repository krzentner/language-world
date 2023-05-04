

```
def robot.move(to_where):  # move robot to the location described by `to_where`
def robot.drop(what):  # drop what the robot is holding
def robot.place(what_where):  # place what the robot is holding where described by `what_where`
def robot.grab(what):  # grab what
def robot.align(what_with_what):  # align what with what described by `what_with_what`
def robot.insert(what_into_what):  # insert what into what described by `what_into_what`
def robot.push(what_how):  # push what as described by `what_how`
def robot.pull(what_how):  # pull what as described by `what_how`
def robot.reach(to_where):  # move gripper to where described by `to_where`
def robot.slide(what_how):  # slide what as described by `what_how`
def robot.close(what):  # close what
def robot.open(what):  # open what
def robot.put(what_where):  # put what where described by `what_where`
def robot.hit(what_with_what):  # hit what with what described by `what_with_what`
```

For example, a robot may be controlled by the code:

```
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```

This can be run as follows:

```
if check("the button is up"):
    button_press_topdown(robot)
```

The functions `button_press_topdown`, `reach`, `door_open`, `drawer_close`,
`drawer_open`, `peg_insert_side`, `pick_place`, `push`, `window_close`, and
`window_open` are provided for you.

## Provided functions: ##

```
def check(condition):
```

You may call `check` with any expression that evaluates to a boolean value.

```
def robot.move(to_where):
```

If the gripper is empty, this moves the gripper as described by `to_where`.

```
def robot.drop(what):
```

This drops whatever the robot is currently holding.

```
def robot.place(what_where