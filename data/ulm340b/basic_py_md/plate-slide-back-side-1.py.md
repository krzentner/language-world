


---

### Part 1: Plate Slide Back Side

We are writing a program to do the following task: `plate-slide-back-side`.

Please write code that begins as follows:

```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not below the plate"):
        robot.place("the gripper below the plate")
    if check("the robot's gripper is below the plate and the robot's gripper is not right of the plate"):
        robot.push("the gripper right towards the plate")
    if check("the robot's gripper is right of the plate"):
        robot.slide("the plate to the goal")
```

---

### Part 2: Window Close

We are writing a program to do the following task: `window-close`.

Please write code that begins as follows:

```
# window-close: slide the window closed to the right
def window_close(robot):
    if check("the robot's gripper is not near the window handle"):
        robot.grab("window handle")
    if check("the robot's gripper is near the window handle"):
        robot.push("window right")
    if check("the robot's gripper is forward aligned with the window handle"):
        robot.push("window right harder")
```

---

### Part 3: Button Press

We are writing a program to do the following task: `button-press-topdown`.

Please write code that begins as follows:

```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not above button"):
        robot.place("the gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")
```

---

### Part 4: Push Puck

We are writing a program to do the following task: `push`.

Please write code that begins as follows:

```
# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check