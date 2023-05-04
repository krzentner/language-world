



**Task 3**

Write a program to perform the task `window-close`.
This task is already partially implemented for you below:

```
# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")
```



**Task 4**

The robot is still in front of the table. Now there is a large green and red button to the left of the robot.
I want to push the red button. Please write a program to perform the task `big-button-press-right`.
Begin with the text:

```
# big-button-press-right: push the large red button from the right
def big_button_press_right(robot):
```



**Task 5**

Now the robot is in front of a door. There is a handle to the right of the robot. I want to pull the door open from the right.
Please write a program to perform the task `door-open-right`.
Begin with the text:

```
# door-open-right: pull the door open from the right
def door_open_right(robot):
```



**Task 6**

Now the robot is in front of a drawer. There is a handle to the right of the robot. I want to pull the drawer open from the right.
Please write a program to perform the task `drawer-open-right`.
Begin with the text:

```
# drawer-open-right: pull the drawer open from the right
def drawer_open_right(robot):
```



**Task 7**

Now there is a peg and a hole to the right of the robot. I want to insert the peg into the hole from the right.
Please write a program to perform the task `peg-insert-right`.
Begin with the text:

```
# peg-insert-right: insert the peg into the hole from the right
def peg_insert_right(robot):
```



**Task 8**

Now there is a drawer with a handle to the left of the robot. I want to close the drawer.
Please write a program to perform the task `drawer-close-left`.
Begin