

"""

if check("the robot's gripper is not near the cube"):
    robot.grab("the cube")
if check("the robot's gripper is not in front of the cube"):
    robot.slide("the cube to the right")
if check("the robot's gripper is near the cube"):
    robot.grab("the cube")


# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    pass


def test_button_press_topdown(robot):
    robot.put("button 5cm above gripper")
    robot.set("gripper open")
    assert button_press_topdown(robot)
    assert robot.get("button is pressed")


def test_drawer_open(robot):
    robot.put("drawer handle 5cm above gripper")
    robot.put("drawer 10cm to the right of gripper")
    robot.set("drawer is closed")
    assert drawer_open(robot)
    assert robot.get("drawer is open")


def test_drawer_close(robot):
    robot.put("drawer handle 5cm above gripper")
    robot.put("drawer 10cm to the right of gripper")
    robot.set("drawer is open")
    assert drawer_close(robot)
    assert robot.get("drawer is closed")


def test_door_open(robot):
    robot.put("door handle 5cm above gripper")
    robot.put("door 10cm to the right of gripper")
    robot.set("door is closed")
    assert door_open(robot)
    assert robot.get("door is open")


def test_window_open(robot):
    robot.put("window handle 5cm above gripper")
    robot.put("window 10cm to the right of gripper")
    robot.set("window is closed")
    assert window_open(robot)
    assert robot.get("window is open")


def test_window_close(robot):
    robot.put("window handle 5cm above gripper")
    robot.put("window 10cm to the right of gripper")
    robot.set("window is open")
    assert window_close(robot)
    assert robot.get("window is closed")


def test_peg_insert