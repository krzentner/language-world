

Your program will be called with:
```
bin_picking(robot)
```

You may also wish to call the following helper functions:
```
robot.move("gripper", to="gripper location")
robot.close("gripper", around="object")
robot.grab("gripper", of="object")
robot.slide("object", to="location")
```

You can use these in `if` statements with `check("CONDITION")` where `CONDITION`
is:
```
gripper is above/below/in front of/behind/left of/right of "OBJECT"
gripper is near/not near "OBJECT"
gripper is vertical/horizontal/forward/backward aligned with "OBJECT"
gripper is around/not around "OBJECT"
gripper is open/closed
```
""".strip()

def test_button_press_topdown(robot):
    robot.reset("button-press-topdown")
    robot.put("gripper", above="button")
    robot.push("down on button")
    robot.step()
    assert robot.status()["buttons"] == ["button:on"]

def test_drawer_close(robot):
    robot.reset("drawer-close")
    robot.grab("drawer handle")
    robot.push("drawer closed")
    robot.step()
    assert robot.status()["buttons"] == ["drawer:closed"]

def test_door_open(robot):
    robot.reset("door-open")
    robot.put("gripper", above="door handle")
    robot.put("gripper", around="door handle")
    robot.pull("door open")
    robot.step()
    assert robot.status()["buttons"] == ["door:open"]

def test_drawer_open(robot):
    robot.reset("drawer-open")
    robot.put("gripper", above="drawer handle")
    robot.put("gripper", around="drawer handle")
    robot.pull("away from drawer")
    robot.step()
    assert robot.status()["buttons"] == ["drawer:open"]

def test_window_close(robot):
    robot.reset("window-close")
    robot.move("gripper", to="left of window handle")
    robot.slide("window right")
    robot.push("window right harder")
    robot.step()
    assert robot.status()["buttons"] ==