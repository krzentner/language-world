

Then write your code below.

```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not vertically aligned with the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not around plate"):
        robot.put("gripper around plate")
    if check("the robot's gripper is around the plate and the plate is not sideways aligned with target location"):
        robot.rotate("plate sideways towards target")
    if check("the plate is sideways aligned with target location and the plate is not moving"):
        robot.push("plate sideways into target")