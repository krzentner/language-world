

And then, write a set of if statements to make the robot slide the window to the left. You can use any of the following descriptions of the robot, the window, and the window handle:

- `robot's gripper`
- `window`
- `window handle`
- `window handle is left of the robot's gripper`
- `window handle is not left of the robot's gripper`
- `robot's gripper is near window handle`
- `robot's gripper is not near window handle`
- `robot's gripper is in front of window handle`
- `robot's gripper is not in front of window handle`


```
# window-open: slide the window open to the left
def window_open(robot):

    # TODO
```
'''

'''
Answer:

# window-open: slide the window open to the left
def window_open(robot):
    if check("window handle is right of the robot's gripper and the robot's gripper is not near window handle"):
        robot.move("gripper to left of window handle")
    if check("robot's gripper is near window handle"):
        robot.slide("window left")
    if check("robot's gripper is in front of window handle"):
        robot.push("window left harder")
'''


'''
Question:

# window-open: slide the window open to the left
def window_open(robot):

    # TODO


# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

'''

'''
Question:

# window-open: slide the window open to the left
def window_open(robot):
    if check("window handle is right of the robot's gripper and the robot's gripper is not near window handle"):
        robot.move("gripper to left of window handle")
    if check("robot's gripper is near window handle"):
        robot.slide("window left")
    if check("