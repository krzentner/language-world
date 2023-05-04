

The following functions are available:

- `check(predicate: str) -> bool`
- `robot.move(goal: str) -> None`
- `robot.grab(object: str) -> None`
- `robot.align(object1: str, object2: str) -> None`
- `robot.place(object: str, location: str) -> None`
- `robot.push(object: str, goal: str) -> None`
- `robot.put(object: str, location: str) -> None`
- `robot.drop(object: str) -> None`
- `robot.insert(object1: str, object2: str) -> None`
- `robot.close(object: str) -> None`
- `robot.slide(object: str, goal: str) -> None`
- `robot.reach(goal: str) -> None`
- `robot.pull(goal: str) -> None`

"""


"""
# soccer: push the soccer ball into the target location
def soccer(robot):
    if check("the robot's gripper is not above soccer ball and the robot's gripper is not vertically aligned with soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not near soccer ball"):
        robot.push("gripper into soccer ball")
    if check("the robot's gripper is near soccer ball and the soccer ball is below the robot's gripper"):
        robot.slide("soccer ball to the goal")

"""


"""
# soccer: push the soccer ball into the target location
def soccer(robot):
    if check("the robot's gripper is not above soccer ball and the robot's gripper is not vertically aligned with soccer ball"):
        robot.put("gripper above soccer ball")
    if check("the robot's gripper is vertically aligned with soccer ball and the robot's gripper is not near soccer ball"):
        robot.push("gripper into soccer ball")
    if check("the robot's gripper is near soccer ball and the soccer ball is below the robot's gripper"):
        robot.slide("soccer ball to the goal")

# window-open: slide the window open to the left
def window_open(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below