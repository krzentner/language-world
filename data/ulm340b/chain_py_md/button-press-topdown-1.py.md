

And add any code below that.

Here are some hints for how to program the task.

  * Steps:
    1. Put the robot gripper roughly above the button
    2. Close the gripper around the button
    3. Push down on the button
  * If the button is above the gripper (from its point of view), move the gripper above the button.
    ```
    # Step 1: Put the robot gripper roughly above the button
    # If the button is above the gripper (from its point of view),
    # move the gripper above the button.
    ```
  * If the gripper is above the button, move the gripper down around the button.
    ```
    # Step 2: Close the gripper around the button
    # If the gripper is above the button, move the gripper down around the
    # button.
    ```
  * If the gripper is around the button and above it, push down on the button to press it.
    ```
    # Step 3: Push down on the button
    # If the gripper is around the button and above it, push down on the button
    # to press it.
    ```
```
# button-press-topdown: push the button down from above
def button_press_topdown(robot):

    # Step 1: Put the robot gripper roughly above the button
    # If the button is above the gripper (from its point of view),
    # move the gripper above the button.
    if check("the button is above the robot's gripper"):
        robot.place("gripper above button")

    # Step 2: Close the gripper around the button
    # If the gripper is above the button, move the gripper down around the
    # button.
    if check("the robot's gripper is above button"):
        robot.put("gripper around button")

    # Step 3: Push down on the button
    # If the gripper is around the button and above it, push down on the button
    # to press it.
    if check("the robot's gripper is around button and the button is above the robot's gripper"):
        robot.push("button down")
```
'''
# button-press-topdown: push the button down from above
def button_press_topdown(robot):