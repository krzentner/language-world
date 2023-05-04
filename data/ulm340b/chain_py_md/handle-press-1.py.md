

In the code above, there are two functions:

```
def check(condition):
```
This function checks whether the condition is true. For example:

```
> check("the robot's gripper is not vertically aligned with door handle")
false
```

You can check the alignment with `left_aligned` and `forward_aligned`. For example:

```
> check("the robot's gripper is left aligned with door handle")
false
> check("the robot's gripper is forward aligned with door handle")
true
```

```
def robot.grab(object_name):
```
This function causes the robot to grab the named object. You can name objects using the following names:

```
"puck"
"peg"
"hole"
"door handle"
"drawer handle"
"handle"
"button"
"window handle"
```

Please name objects only using these names. For example:

```
> robot.grab("door handle")
> check("the robot's gripper is around door handle")
true
> robot.grab("handle")
> check("the robot's gripper is around handle")
true
```

```
def robot.place(object_name, location):
```
This function causes the robot to place the named object at the named location. You can name locations using the following names:

```
"reach target"
"goal"
"button"
"handle"
```

Please name locations only using these names. For example:

```
> robot.grab("button")
> robot.place("button", "button")
> check("the robot's gripper is not around button")
true
> check("the robot's gripper is not around handle")
true
> check("button is at button")
true
```

```
def robot.close():
```
This function causes the robot to close its gripper. For example:

```
> robot.grab("handle")
> robot.close()
> check("the robot's gripper is closed")
true
```

```
def robot.open():
```
This function causes the robot to open its gripper. For example:

```
> robot.grab("handle")
> robot.close()
> robot.open()
> check("the robot's gripper is open")
true
```

```
def robot.move(object_name, location):
```
This function causes the robot to move the object to the location.
This function does not allow the robot to grab the object.

For example:

```
> robot.