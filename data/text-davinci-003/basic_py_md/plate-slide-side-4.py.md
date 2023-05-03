

Then, fill in the code:

```
# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("plate is not left of the robot's gripper and plate is not forward aligned with the robot's gripper"):
        robot.grab("plate")
    if check("the robot's gripper is forward aligned with the plate and plate is not horizontally aligned with goal"):
        robot.align("plate to goal")
    if check("plate is horizontally aligned with goal"):
        robot.slide("plate to goal")
```