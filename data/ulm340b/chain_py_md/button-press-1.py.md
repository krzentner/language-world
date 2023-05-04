

Now, your goal is to move the robot so that its gripper is aligned with the button from the front.
Then you want to push on the button. You may also want to move the robot back afterwards.
I will show you a demo.`

### Explanation:

We want a program to move the robot's gripper to be aligned with the button from the front, push the button, then move the robot back.

```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push on the button
    #  3. Move robot back
    # The gripper should move from left to right.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move("gripper to the button")
    # Push on the button.
    # We should also open the gripper.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("on the button")
    # Move robot back so that the gripper is out of the way.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move("robot backwards")
```

### Variation:

We can also move the robot from right to left.

```
# button-press: push the button from the front
def button_press(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the front
    #  2. Push on the button
    #  3. Move robot back
    # The gripper should move from right to left.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move("gripper to the button")
    # Push on the button.
    # We should also open the gripper.
    if check("the robot's gripper is horizontally aligned with button"):
        robot.push("on the button")
    # Move robot back so that the gripper is out of the way.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move("robot backwards")
```

### Explanation:

Now, your goal is to pick up the block and move it to the target location.
You may want to use the "align" command