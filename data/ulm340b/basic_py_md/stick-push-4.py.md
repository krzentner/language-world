

The `robot` object has methods for moving the gripper:

```
robot.move("the gripper to left of the ball")
robot.move("the gripper to right of the ball")
robot.put("the gripper above the ball")
robot.grab("the ball")
robot.release("the ball")
```

It also has methods for performing different types of motions:

```
robot.slide("the ball to the goal")
robot.push("the ball into the box")
robot.reach("into the box")
robot.insert("the ball into the box")
```
"""
def stick_push(robot):
    if check("the robot's gripper is not above the thermos"):
        robot.put("the gripper above the thermos")
    if check("the robot's gripper is above the thermos and the robot's gripper is not around the thermos"):
        robot.put("the gripper around the thermos")
    if check("the robot's gripper is near the thermos and the robot's gripper is open"):
        robot.grab("the thermos")
    if check("the robot's gripper is above the thermos and the robot's gripper is closed"):
        robot.slide("the thermos to the goal")
    if check("the thermos is not above the box and the thermos is not vertically aligned with the box"):
        robot.put("the thermos above the box")
    if check("the thermos is above the box and the thermos is not in the box"):
        robot.push("the thermos into the box")


if __name__ == "__main__":
    TASK_1 = "button-press-topdown"
    TASK_2 = "drawer-open"
    TASK_3 = "door-open"
    TASK_4 = "drawer-close"
    TASK_5 = "window-open"
    TASK_6 = "window-close"
    TASK_7 = "peg-insert-side"
    TASK_8 = "reach"
    TASK_9 = "push"
    TASK_10 = "pick-place"
    TASK_11 = "stick-push"
    print(TASK_11)
    print("\n".join(globals()[TASK_11](robot=robot)))


# button-press-topdown: push the button down from above
# drawer-open: pull the drawer open
# door-open: pull the door open
# drawer-close: push the drawer close