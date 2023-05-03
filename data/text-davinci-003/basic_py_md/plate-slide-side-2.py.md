

Solution: 

```
# plate-slide-side: slide the plate sideways into the target location
def plate_slide_side(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not forward aligned with the plate"):
        robot.align("gripper with plate")
    if check("the robot's gripper is forward aligned with plate and the plate is not near goal"):
        robot.push("plate towards goal")
    if check("plate is almost near goal"):
        robot.slide("plate into goal")
```