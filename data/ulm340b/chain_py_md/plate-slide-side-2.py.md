

This is a bit more challenging: while for each other program, there is only one
target object (which you can refer to as `the x` or `x`), the target object in
this program is a plate, which is a flat surface.  We can only refer to it as
"a plate" or "the plate" and you must infer which plate from context.

The plate should be aligned with the target location from the front and then
be moved sideways into the target location.

The plate should be pushed by the gripper, like a sliding hockey puck.

Here is some example output:
```
# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the plate is not right of robot"):
        robot.move("gripper right of plate")
    if check("gripper is not forward aligned with plate and robot's gripper is not near plate"):
        robot.push("gripper into plate")
    if check("robot's gripper is near plate and plate is forward aligned with gripper"):
        robot.slide("plate to the goal")
```

Please type your code here:

```python
# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    # Steps:
    #  1. Put gripper left of the plate
    #  2. Start pushing against the plate
    #  3. Push the plate to the target location

    if check("the robot's gripper is not right of the plate"):
        robot.put("the robot's gripper right of the plate")

    if check("the robot's gripper is not near the plate and the plate is not left of the robot's gripper and the plate is not forward aligned with the robot's gripper"):
        robot.move("the robot's gripper forward to the plate")

    if check("the plate is left of the robot's gripper and the plate is forward aligned with the robot's gripper and the robot's gripper is near the plate"):
        robot.slide("the plate to the goal")
```
"""


def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.