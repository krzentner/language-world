

Your robot will need to be able to perform a number of actions.
It can use: `move("thing to somewhere")`, `grab("thing")`,
`put("thing somewhere")`, `slide("thing to somewhere")`,
`push("thing to somewhere")`, `pull("thing from somewhere")`,
`reach("to somewhere")`, and `insert("thing into somewhere")`.

Your robot can also check conditions, such as:
`check("thing is not left of something")`, `check("thing is left of something")`, `check("thing is near something")`,
`check("thing is not near something")`, `check("thing is forward aligned with something")`, `check("thing is not forward aligned with something")`,
`check("thing is vertically aligned with something")`, `check("thing is not vertically aligned with something")`,
`check("thing is horizontally aligned with something")`, `check("thing is not horizontally aligned with something")`,
`check("thing is almost vertically aligned with something")`, `check("thing is not almost vertically aligned with something")`.

Here's some sample code that you might find helpful:

```
if check("thing is not left of something"):
    robot.move("thing to left of something")

if check("thing is forward aligned with something and thing is not near something"):
    robot.push("thing closer to something")
```

You can see the code you wrote so far by writing `check_code()`, and can start over by writing `restart()`.

If you feel like you need inspiration, writing `hint()` will also help.

Please press the DONE button once you're finished with the program.
"""


# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above