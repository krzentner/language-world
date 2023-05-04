

To get the robot to reach to the faucet:

```
if check("the robot's gripper is not near faucet"):
    robot.reach("to the faucet")
```

You can also give this task to the `reach` function:

```
if check("the robot's gripper is not near faucet"):
    reach("to the faucet")
```

To grab the faucet:

```
if check("the robot's gripper is near faucet"):
    robot.grab("faucet")
```

If the faucet is closed:

```
if check("faucet is closed"):
    robot.turn("faucet handle left")
```

Putting this all together:

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is not near faucet"):
        reach("to the faucet")
    if check("the robot's gripper is near faucet"):
        robot.grab("faucet")
    if check("faucet is closed"):
        robot.turn("faucet handle left")
```

To make sure that this works:

```
faucet_open(robot)
```

We have now covered all of the tasks for this experiment.
Here is a summary of the skills that your robot can do:

```
# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to