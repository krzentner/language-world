

I will run your code using the command:

```
robot = make_robot_simulator()
coffee_push(robot)
```

This gives you the chance to test your code before submitting.

```python
# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Grab handle by moving gripper down and closing it
    #  3. Lift mug
    #  4. Line up the mug over target location
    #  5. Drop mug
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the gripper is vertically aligned with the handle, it should be able to
    # grab it.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open"):
        robot.move_gripper("above the handle", close_gripper=True)
    # If the gripper is above the handle, it can grab the handle by closing.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("forward aligned with the handle")
    # Once the gripper has the mug, we can move it.
    if check("the robot's gripper is near the handle"):
        robot.move_gripper("almost vertically aligned with the handle")
    # Line up the gripper with the target location.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("vertically aligned with the target location")
```
"""

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=